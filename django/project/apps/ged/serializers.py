
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from ged.models import Basket
from ged.models import Document
from ged.models import UploadFile
from ged.models import Folder


from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class BasketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Basket
        fields = ('code', 'libelle', 'description')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'name', 'path', 'contentType', 'created_at',
                  'updated_at', 'version', 'basket')


class UploadFileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UploadFile
        fields = ('name', 'created_at', 'updated_at')


class FolderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Folder
        fields = (
            'id', 'libelle', 'node_l', 'node_r', 'created_at', 'updated_at')
