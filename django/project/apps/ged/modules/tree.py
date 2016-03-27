
from django.db.models import F
from django.core.exceptions import ValidationError
from ged.models import Folder

from rest_framework import serializers


class Tree:

    def find(self, id):

        f = Folder.objects.get(pk=id)

        return f

    # def create(self, right, left, libelle):
        # folder = Folder.create(right, left, libelle)
        # folder.save()
        # return folder

    def findRoot(self):

        folder = Folder.objects.get(node_l=1)
        return folder

    def createRoot(self, libelle):

        folder = Folder.create(1, 2, libelle)
        folder.save()
        return folder

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
        print("get")
        Folder.objects.filter(
            node_l__gte=folder.node_l, node_r__lte=folder.node_r).delete()
        print("get1")
        Folder.objects.filter(node_r__gte=node_r).update(
            node_r=F('node_r') - decalage)
        print("get2")
        Folder.objects.filter(node_l__gt=node_l).update(
            node_l=F('node_l') - decalage)

        pass
    # def removeElement(self, id):

        # folder = Folder.objects.get(pk=id)

        # Folder.objects.filter(node_l__gte=folder.node_l).update(
        #    node_l=F('node_l') - 2)

        # Folder.objects.filter(node_r__gte=folder.node_l).update(
        #     node_r=F('node_r') - 2)

        # folder.delete()

    def buildTree(self):

        folders = Folder.objects.all().prefetch_related(
            'parent').order_by('node_l')

        # folders = Folder.objects.all().order_by('node_l')

        parents = {}
        tree = []
        for folder in folders:
            if folder.parent_id is None:
                root = TreeFolder(folder)
                parents[folder.id] = root
                tree.append(root)
            else:
                node = TreeFolder(folder)
                parent = parents[folder.parent_id]
                parent.items.append(node)
                parents[folder.id] = node

        return tree


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
