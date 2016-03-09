import datetime
import sys

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from ged.models import Basket
from ged.models import Document
from ged.models import UploadFile
from ged.models import Folder

from ged.modules.tree import TreeSerializer

from ged.serializers import UserSerializer
from ged.serializers import GroupSerializer
from ged.serializers import BasketSerializer
from ged.serializers import DocumentSerializer
from ged.serializers import UploadFileSerializer
from ged.serializers import FolderSerializer

from ged.modules.tree import Tree

from rest_framework import authentication
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
# from rest_framework import renderers
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.permissions import AllowAny

from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from rest_framework.response import Response
from rest_framework import status


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # renderer_classes = (JSONRenderer, HTMLFormRenderer
    #    , BrowsableAPIRenderer )


class GroupViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FolderViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class TreeViewSetDetail(viewsets.ViewSet):

    def list(self, request):

        pass

    def destroy(self, request, pk=None):

        pass

    def create(self, request):

        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

        # return Response({}, status=status.HTTP_400_BAD_REQUEST)


class TreeViewSet(viewsets.ViewSet):

    http_method_names = ['get', 'post', 'head', 'delete']

    def list(self, request):
        queryset = Tree().buildTree()
        serializer = TreeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        print(request.data)

        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            print(serializer.data)
            root = Folder.objects.get(pk=request.data['id'])
            tree = Tree()
            folder = tree.createChild(root.id, serializer.data['libelle'])

            return Response(FolderSerializer(folder).data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
            tree = Tree()
            tree.remove(pk)
            return Response({"status": "succces"},
                            status=status.HTTP_201_CREATED)
        except:

            print(sys.exc_info())
            return Response({"status": "error"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass


class BasketViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (permissions.AllowAny,)

    @list_route(methods=['get', ])
    def code(self, request, pk=None):

        snippet = pk
        return Response(snippet)

    @detail_route(methods=['get', ])
    def accounts(self, request, pk):

        snippet = "Highlight"
        return Response(snippet)


class SnippetList(generics.ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer


class BasketViewByCodeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Basket to be viewed or edited.
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # code = self.kwargs['code']
        # return Basket.objects.filter(code=code)
        queryset = Basket.objects.all()
        code = self.request.query_params.get('code', None)
        if code is not None:
            queryset = queryset.filter(code=code)
        return queryset


class DocumentViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
