import datetime   

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from mysite.apps.notes.models import Note
from mysite.apps.notes.models import ReSTNote

from mysite.apps.notes.serializers import UserSerializer
from mysite.apps.notes.serializers import GroupSerializer
from mysite.apps.notes.serializers import NoteSerializer
from mysite.apps.notes.serializers import ReSTNoteSerializer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
   # renderer_classes = (JSONRenderer, HTMLFormRenderer, BrowsableAPIRenderer )

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ReSTNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ReSTNote.objects.all()
    serializer_class = ReSTNoteSerializer



