
# from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from drive.models import Basket
from drive.models import Document

from drive.serializers import UserSerializer
from drive.serializers import GroupSerializer
from drive.serializers import BasketSerializer
from drive.serializers import DocumentSerializer

from rest_framework import viewsets
# from rest_framework import renderers
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from rest_framework.response import Response

from drive.paginators import StandardResultsSetPagination


from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

import sys
from drive import settings

from drive.mptt import TreeSerializer
from drive.mptt import Tree
# from drive.views import DefaultsAuthentificationMixin

from drive.models import DriveNode
from drive.serializers import DriveNodeSerializer


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


class AuthentificationViewSet(viewsets.ViewSet):

    """
    API endpoint that allows Authnetification in the drive .
    """

    def list(self, request):

        Session.objects.all().delete()
        # raise ValidationError({'detail': 'not implemented yet'})

        return Response({'detail': 'connected'},
                        status=status.HTTP_201_CREATED)

    def create(self, request):
        """
        API endpoint that allows Authnetification in the drive .
        """
        username = request.data['username']
        password = request.data['password']

        try:
            # user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
        except user.DoesNotExist:
            raise ValidationError('detail', 'unknown user')

        if user is not None:
            if user.is_active is False:
                # login(request, user)
                raise ValidationError('detail', 'Disabled account')
            else:
                token = Token.objects.get_or_create(user=user)
                print(token.key)
        else:
            raise ValidationError('detail', 'unknown user')

        return Response({'detail': token.__str__})


# class FolderDocumentViewSet(DefaultsAuthentificationMixin, viewsets.ViewSet):

#     http_method_names = ['get', 'post', 'head', 'delete']
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer

#     def list(self, request):

#         folderId = request['id']
#         if folderId is not None:
#             queryset = queryset.filter(folder_id=folderId)

# return Response(serializer.data)

#     def create(self, request):
#         pass

#     def destroy(self, request, pk=None):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

class DriveNodeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DriveNode.objects.all()
    serializer_class = DriveNodeSerializer


class DriveViewSet(viewsets.ViewSet):

    _tree = Tree(settings.TREE_ROOT_NAME)

    def list(self, request, username=None):
        """
        API endpoint that allows to get the user folders as Tree .
        """

        if username:

            if username == 'root':
                queryset = self._tree.buildTree()
            else:

                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    # raise ValidationError('detail', 'invalid request data')
                    return Response(
                        {"status": "user does not exists : " + username},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                queryset = self._tree.buildUserTree(username)

        serializer = TreeSerializer(queryset, many=True)
        return Response(serializer.data)

    # @list_route()
    # @detail_route(methods=['get'])
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

    def create(self, request, username):
        """
        API Create user root node.
        """
        root = self._tree.getRoot()
        pk = request.data['username']
        self._tree.createChild(root.id, pk)

        queryset = self._tree.buildUserTree(pk)
        serializer = TreeSerializer(queryset, many=True)

        return Response(serializer.data)


class DriveFolderViewSet(viewsets.ViewSet):

    http_method_names = ['get', 'post', 'head', 'delete']

    _tree = Tree(settings.TREE_ROOT_NAME)

    def list(self, request, username):

        # queryset = self._tree.buildUserTree(username, True)
        # serializer = TreeSerializer(queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        root = self._tree.getUserRoot(username)
        return Response(DriveNodeSerializer(root).data,
                        status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def children(self, request, username, pk):

        queryset = self._tree.getChildren(pk)
        serializer = DriveNodeSerializer(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def documents(self, request, username=None, pk=None):

        queryset = Document.objects.all()
        # folderId = self.request.query_params.get('id', None)
        if pk is not None:
            queryset = queryset.filter(folder_id=pk)

        serializer = DocumentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, username):

        serializer = DriveNodeSerializer(data=request.data)
        if serializer.is_valid():

            parent = DriveNode.objects.get(pk=request.data['id'])

            if parent is None:
                raise ValidationError(
                    'invalid request data parent is none')

            else:
                folder = self._tree.createChild(
                    parent.id, serializer.data['libelle'])

            return Response(DriveNodeSerializer(folder).data,
                            status=status.HTTP_201_CREATED)

        raise ValidationError('invalid request data')

    def destroy(self, request, username, pk=None):

        try:
            self._tree.remove(pk)
            return Response({"status": "succces"},
                            status=status.HTTP_201_CREATED)
        except:
            print(sys.exc_info())
            raise ValidationError('invalid request data')

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass


class DriveTreeFolderViewSet(viewsets.ViewSet):

    _tree = Tree(settings.TREE_ROOT_NAME)

    def list(self, request, username=None):

        if username:

            if username == 'root':
                queryset = self._tree.buildTree()
            else:

                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    exc_type, exc_value, exc_traceback = sys.exc_info()

                    return Response(
                        {"status": "user does not exists : " + username},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                queryset = self._tree.buildUserTree(username)

        serializer = TreeSerializer(queryset, many=True)
        return Response(serializer.data)
