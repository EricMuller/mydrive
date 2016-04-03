
from django.db.models import F
from django.core.exceptions import ValidationError
from backdrive.models import Folder

from rest_framework import serializers

# Arbre intervallaire


class Tree:

    def __init__(self, rootName):
        self._rootName = rootName

    def find(self, id):
        f = Folder.objects.get(pk=id)
        return f

    def getRoot(self):
        try:
            folder = Folder.objects.get(node_l=1)
        except Folder.DoesNotExist:
            folder = self._createRoot()

        return folder

    def _createRoot(self):

        folder = Folder.create(1, 2, self._rootName)
        folder.save()
        return folder

    def createUserRoot(self, libelle):

        root = getRoot()

    def createChild(self, id, libelle):

        parent = Folder.objects.get(pk=id)

        Folder.objects.filter(node_r__gte=parent.node_r).update(
            node_r=F('node_r') + 2)

        Folder.objects.filter(node_l__gte=parent.node_r).update(
            node_l=F('node_l') + 2)

        folder = Folder.create(
            parent.node_r, parent.node_r + 1, libelle, parent)

        folder.save()

        return folder

    def remove(self, id):

        folder = Folder.objects.get(pk=id)

        decalage = folder.node_r - folder.node_l + 1

        node_r = folder.node_r
        node_l = folder.node_l

        Folder.objects.filter(
            node_l__gte=folder.node_l, node_r__lte=folder.node_r).delete()

        Folder.objects.filter(node_r__gte=node_r).update(
            node_r=F('node_r') - decalage)

        Folder.objects.filter(node_l__gt=node_l).update(
            node_l=F('node_l') - decalage)

        pass

    def buildUserTree(self, username):
        tree = []
        try:
            root = Folder.objects.get(node_l=1)

            user = Folder.objects.filter(
                libelle=username, parent_id=root.id).first()

            if user is not None:
                print('user=' + str(user.id))

                folders = Folder.objects.filter(
                    node_l__gte=user.node_l, node_r__lte=user.node_r).all(
                ).prefetch_related('parent').order_by('node_l')
                tree = self._build(folders, user.id)

        except Folder.DoesNotExist:
            pass

        return tree

    def buildTree(self):
        tree = []
        try:
            root = Folder.objects.get(node_l=1)
            folders = Folder.objects.all().prefetch_related(
                'parent').order_by('node_l')
            tree = self._build(folders, root.id)
        except:
            pass
        return tree

    def _build(self, folders, root_id):

        # folders = Folder.objects.all().order_by('node_l')

        parentsDic = {}
        tree = []
        for folder in folders:
            print(folder.id, root_id)
            if folder.id == root_id:
                root = TreeFolder(folder)
                parentsDic[folder.id] = root
                tree.append(root)
            else:
                node = TreeFolder(folder)
                parent = parentsDic[folder.parent_id]
                print(parent.id)
                parent.items.append(node)
                parentsDic[folder.id] = node

        return tree
    # def removeElement(self, id):

        # folder = Folder.objects.get(pk=id)

        # Folder.objects.filter(node_l__gte=folder.node_l).update(
        #    node_l=F('node_l') - 2)

        # Folder.objects.filter(node_r__gte=folder.node_l).update(
        #     node_r=F('node_r') - 2)

        # folder.delete()


class TreeFolder():

    def __init__(self, folder):
        self.id = folder.id
        self.node_l = folder.node_l
        self.node_r = folder.node_r
        self.libelle = folder.libelle
        self.updated_at = folder.updated_at
        self.items = []
        self.parent_id = folder.parent_id


class Items(object):

    items = []

    def __init__(self, items):
        self.items = items


class ItemField(serializers.Field):

    def to_internal_value(self, data):
        if isinstance(data, list):
            return Items(data)
        else:
            msg = self.error_messages['invalid']
            raise ValidationError(msg)

    def to_representation(self, value):

        # value = json.dumps(value)
        values = []
        for tree in value:
            serializer = TreeSerializer(tree)
            values.append(serializer.data)
            pass

        return values


class TreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    libelle = serializers.CharField(max_length=30)
    items = ItemField()

    class Meta:
        model = TreeFolder
        fields = (
            'id', 'parent_id', 'libelle', 'items')
