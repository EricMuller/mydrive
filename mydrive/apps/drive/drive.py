

from django.db.models import F
from django.db.models import Q
from django.core.exceptions import ValidationError
from rest_framework import serializers
from drive.models import Repository
from django.db import transaction
# Arbre intervallaire


class Mptt:

    def __init__(self, rootName):
        self._rootName = rootName

    def getworkspace(self, username):

        try:
            root = Repository.objects.get(node_l=1)
            user = Repository.objects.filter(
                libelle=username, parent_id=root.id).first()
            return user
        except:
            return None

    def getRoot(self):
        try:
            repository = Repository.objects.get(node_l=1)
        except Repository.DoesNotExist:
            repository = self._createRoot()

        return repository

    def _createRoot(self):

        repository = Repository.create(1, 2, self._rootName)
        repository.save()
        return repository

    def createUserRoot(self, libelle):

        self.getRoot()

    def getChildren(self, id):

        parent = Repository.objects.get(pk=id)

        repositories = Repository.objects.filter(
            parent_id=parent.id).all(
        ).prefetch_related('parent').order_by('node_l')

        return repositories

    @transaction.non_atomic_requests
    def createChild(self, id, libelle):

        parent = Repository.objects.get(pk=id)

        Repository.objects.filter(node_r__gte=parent.node_r).update(
            node_r=F('node_r') + 2)

        Repository.objects.filter(node_l__gte=parent.node_r).update(
            node_l=F('node_l') + 2)

        repository = Repository.create(
            parent.node_r, parent.node_r + 1, libelle, parent)

        repository.save()

        return repository

    def remove(self, id):

        repository = Repository.objects.get(pk=id)

        decalage = repository.node_r - repository.node_l + 1

        node_r = repository.node_r
        node_l = repository.node_l

        Repository.objects.filter(
            node_l__gte=repository.node_l,
            node_r__lte=repository.node_r).delete()

        Repository.objects.filter(node_r__gte=node_r).update(
            node_r=F('node_r') - decalage)

        Repository.objects.filter(node_l__gt=node_l).update(
            node_l=F('node_l') - decalage)

        pass

    def getRepository(self, id):
        repository = Repository.objects.get(pk=id)
        return repository

    def getRepositories(self):
        repositories = Repository.objects.all().prefetch_related(
            'parent').order_by('node_l')
        return repositories

    def getUserRepositories(self, workspace, lazy=False):

        repositories = []

        try:

            if workspace is not None:
                if not lazy:
                    repositories = Repository.objects.filter(
                        node_l__gte=workspace.node_l,
                        node_r__lte=workspace.node_r).all(
                    ).prefetch_related('parent').order_by('node_l')

                else:
                    repositories = Repository.objects.filter(
                        Q(parent_id=workspace.id) | Q(id=workspace.id)).all(
                    ).prefetch_related('parent').order_by('node_l')

        except Repository.DoesNotExist:
            pass

        return repositories


class Storage:

    def buildPathforNode(self, repository):

        pass
        # SELECT *   FROM MATABLE
        #         WHERE BG <= :BG_Feuille AND BD >= DB_Feuille
        #             ORDER BY BG


class Drive(Mptt):

    def __init__(self, rootName):
        super().__init__(rootName)

    def buildUserTree(self, username, lazy=False):

        tree = []
        workspace = self.getworkspace(username)
        if workspace is not None:
            repositories = self.getUserRepositories(workspace, lazy)
            if repositories is not None:
                tree = self._build(repositories, workspace.id)

        return tree

    def buildTree(self):
        tree = []
        try:
            root = self.getRoot()
            repositories = self.getRepositories()
            if repositories is not None:
                tree = self._build(repositories, root.id)
        except:
            pass
        return tree

    def _build(self, repositories, root_id):

        # folders = Folder.objects.all().order_by('node_l')
        parentsDic = {}
        drive = []
        for repository in repositories:
            print(repository.id, root_id)
            if repository.id == root_id:
                root = RepositoryNode(repository)
                parentsDic[repository.id] = root
                drive.append(root)
            else:
                node = RepositoryNode(repository)
                parent = parentsDic[repository.parent_id]
                print(parent.id)
                parent.items.append(node)
                parentsDic[repository.id] = node

        return drive
    # def removeElement(self, id):

        # folder = Folder.objects.get(pk=id)

        # Folder.objects.filter(node_l__gte=folder.node_l).update(
        #    node_l=F('node_l') - 2)

        # Folder.objects.filter(node_r__gte=folder.node_l).update(
        #     node_r=F('node_r') - 2)

        # folder.delete()


class RepositoryNode():

    def __init__(self, repo):
        self.id = repo.id
        self.node_l = repo.node_l
        self.node_r = repo.node_r
        self.libelle = repo.libelle
        self.updated_at = repo.updated_at
        self.items = []
        self.parent_id = repo.parent_id


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
            serializer = DriveSerializer(tree)
            values.append(serializer.data)
            pass

        return values


class DriveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    libelle = serializers.CharField(max_length=30)
    items = ItemField()

    class Meta:
        model = RepositoryNode
        fields = (
            'id', 'parent_id', 'libelle', 'items')
