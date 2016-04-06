
import sys
import traceback

# from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from backdrive import settings
from backdrive.models import Basket
from backdrive.models import Document
from backdrive.models import Folder

from backdrive.modules.tree import TreeSerializer
from backdrive.modules.tree import Tree

from backdrive.serializers import UserSerializer
from backdrive.serializers import GroupSerializer
from backdrive.serializers import BasketSerializer
from backdrive.serializers import DocumentSerializer

from backdrive.serializers import FolderSerializer

from backdrive.views import DefaultsAuthentificationMixin


from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import status

# from rest_framework import renderers
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.permissions import AllowAny


from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from rest_framework.response import Response

from backdrive.paginators import StandardResultsSetPagination


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


class TreeViewSet(viewsets.ViewSet):

    _tree = Tree(settings.TREE_ROOT_NAME)

    def list(self, request, pk=None):
        queryset = self._tree.buildTree()
        serializer = TreeSerializer(queryset, many=True)
        return Response(serializer.data)

    # @list_route()
    @detail_route(methods=['get'])
    def plan(self, request, pk=None):
        try:
            User.objects.get(username=pk)
        except User.DoesNotExist:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # raise ValidationError('detail', 'invalid request data')
            return Response({"status": "user does not exists : " + pk},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        queryset = self._tree.buildUserTree(pk)
        serializer = TreeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        root = self._tree.getRoot()
        pk = request.data['username']
        self._tree.createChild(root.id, pk)

        queryset = self._tree.buildUserTree(pk)
        serializer = TreeSerializer(queryset, many=True)

        return Response(serializer.data)


class TreeFolderViewSet(viewsets.ViewSet):

    http_method_names = ['get', 'post', 'head', 'delete']

    _tree = Tree(settings.TREE_ROOT_NAME)

    def create(self, request):

        print(request.data)
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():

            parent = Folder.objects.get(pk=request.data['id'])

            folder = self._tree.createChild(
                parent.id, serializer.data['libelle'])

            return Response(FolderSerializer(folder).data,
                            status=status.HTTP_201_CREATED)
        raise ValidationError('detail', 'invalid request data')

    def destroy(self, request, pk=None):

        try:
            self._tree.remove(pk)
            return Response({"status": "succces"},
                            status=status.HTTP_201_CREATED)
        except:
            print(sys.exc_info())
            raise ValidationError('detail', 'invalid request data')

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
    # permission_classes = (permissions.AllowAny,)

    @list_route(methods=['get', ])
    def code(self, request, pk=None):

        snippet = pk
        return Response(snippet)

    @detail_route(methods=['get', ])
    def accounts(self, request, pk):

        snippet = "Highlight"
        return Response(snippet)


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
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Document.objects.all()
        folderId = self.request.query_params.get('id', None)

        if folderId is not None:
            queryset = queryset.filter(folder_id=folderId)

        return queryset


class FolderDocumentViewSet(DefaultsAuthentificationMixin, viewsets.ViewSet):

    http_method_names = ['get', 'post', 'head', 'delete']
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def list(self, request):

        folderId = request['id']
        if folderId is not None:
            queryset = queryset.filter(folder_id=folderId)

        # return Response(serializer.data)

    def create(self, request):
        pass

    def destroy(self, request, pk=None):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass
