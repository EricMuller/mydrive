
from django.contrib.auth.models import User, Group
from mysite.apps.notes.models import Note
from mysite.apps.notes.models import ReSTNote
from rest_framework import serializers

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id','titre', 'description', 'email')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')        


class ReSTNoteSerializer(serializers.ModelSerializer):
    #reStText = serializers.HyperlinkedIdentityField(view_name='services')
   class Meta:
        model = ReSTNote
        fields = ('id','titre','codeSystem','codeLangage','reStText')
