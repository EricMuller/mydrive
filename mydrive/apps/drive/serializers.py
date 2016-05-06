
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from drive.models import Basket
from drive.models import File
from drive.models import UploadFile
from drive.models import Repository


# from drive.models import Foo


from rest_framework import serializers
# from swampdragon.serializers.model_serializer import ModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        # https://github.com/tomchristie/django-rest-framework/issues/2760
        extra_kwargs = {'url': {'view_name': 'internal_apis:user-detail'}}


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class BasketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Basket
        fields = ('code', 'libelle', 'description')


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'name', 'path', 'contentType', 'created_at',
                  'updated_at', 'version', 'repository')


class UploadFileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UploadFile
        fields = ('name', 'created_at', 'updated_at')


class RepositorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Repository
        fields = (
            'id', 'libelle', 'node_l', 'node_r', 'created_at', 'updated_at')

# class FooSerializer(ModelSerializer):

#     class Meta:
#         model = Foo
#         publish_fields = ('text', )
#         update_fields = ('text', )
