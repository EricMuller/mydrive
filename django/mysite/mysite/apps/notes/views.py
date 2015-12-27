import datetime   

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.template import Context
from django.template.loader import get_template
from mysite.apps.notes.models import Note
from mysite.apps.notes.models import ReSTNote
from mysite.apps.notes.serializers import UserSerializer
from mysite.apps.notes.serializers import  GroupSerializer
from mysite.apps.notes.serializers import NoteSerializer
from mysite.apps.notes.serializers import ReSTNoteSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.renderers import BrowsableAPIRenderer

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #renderer_classes = (JSONRenderer,  HTMLFormRenderer )
   # renderer_classes = (JSONRenderer, BrowsableAPIRenderer )



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

def home(request):
    return render_to_response("index.html", RequestContext(request, {}))

def index(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
#    now = datetime.datetime.now()
#    t = get_template('notes/index.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
     return render_to_response("notes/index.html", RequestContext(request, {}))    

     