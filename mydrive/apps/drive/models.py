from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
# from django.utils import timezone
# from swampdragon.models import SelfPublishModel


class DateModel(models.Model):

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # user_created = models.ForeignKey(
    #     User, related_name='%(class)s_user_created', default=None)
    # user_updated = models.ForeignKey(
    #     User, related_name='%(class)s_user_updated', default=None)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.user_created_id is None:
    #         self.user_created = User.objects.get(username='eric_muller')
    #         self.user_updated = User.objects.get(username='eric_muller')
    #     else:
    #         self.user_updated = User.objects.get(username='eric_muller')

    #     super(DateModel, self).save(
    #         force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Node(DateModel):

    node_l = models.IntegerField(default=0)
    node_r = models.IntegerField(default=0)
    libelle = models.CharField(max_length=256)
    parent = models.ForeignKey("self", null=True, default=None, blank=True)

    class Meta:
        abstract = True


class DriveNode(Node):
    # groups = models.ManyToManyField(Group)
    # download = models.BooleanField(default=True)
    def __str__(self):
        return self.libelle

    @classmethod
    def create(cls, node_l, node_r, libelle, parent=None):
        folder = cls(
            node_l=node_l, node_r=node_r, libelle=libelle,
            parent=parent)

        return folder


class Basket(DateModel):
    code = models.CharField(primary_key=True, max_length=30)
    libelle = models.CharField(max_length=30)
    description = models.CharField(max_length=256)

    @classmethod
    def create(cls, code, libelle, description):
        basket = cls(code=code, libelle=libelle, description=description)
        return basket

    def __str__(self):
        return self.libelle


class UploadFile(DateModel):

    name = models.CharField(max_length=256, default=None)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Document(DateModel):

    """docstring for ClassName"""
    name = models.CharField(max_length=256)
    path = models.CharField(max_length=512)
    contentType = models.CharField(max_length=30)
    version = models.IntegerField(default=0)
    folder = models.ForeignKey(
        DriveNode, verbose_name='DriveNode', null=True,
        default=None, blank=True)

    @classmethod
    def create(cls, name, path, contentType, version, folder):
        document = cls(
            name=name, path=path, contentType=contentType,
            version=version, folder=folder)
        return document


# class Foo(SelfPublishModel, models.Model):
#     serializer_class = 'drive.serializers.FooSerializer'
#     text = models.CharField(max_length=100)
