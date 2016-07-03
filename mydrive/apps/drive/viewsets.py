
# from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from drive.models import Basket
from drive.models import File

from drive.serializers import UserSerializer
from drive.serializers import GroupSerializer
from drive.serializers import BasketSerializer
from drive.serializers import FileSerializer

from rest_framework import viewsets
# from rest_framework import renderers
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from rest_framework.response import Response

from drive.paginators import StandardResultsSetPagination
from drive.paginators import LargeResultsSetPagination


# from django.contrib.auth import authenticate
# from django.contrib.sessions.models import Session
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

import sys
from drive import settings

# from drive.drive import DriveSerializer
from drive.drive import Drive
from drive.drive import RepositoryNode
from drive.drive import RepositoryNodeSerializer

# from drive.views import DefaultsAuthentificationMixin

from drive.models import Repository
from drive.serializers import RepositorySerializer
from drive.serializers import CreateRepositorySerializer

from drive.constants import DriveConstants
import json


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


class FileViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = File.objects.all()
        repositoryId = self.request.query_params.get('id', None)

        if repositoryId is not None:
            queryset = queryset.filter(repository_id=repositoryId)

        return queryset


# class AuthentificationViewSet(viewsets.ViewSet):

#     """
#     API endpoint that allows Authnetification in the drive .
#     """

#     def list(self, request):

#         Session.objects.all().delete()
#         # raise ValidationError({'detail': 'not implemented yet'})

#         return Response({'detail': 'connected'},
#                         status=status.HTTP_201_CREATED)

#     def create(self, request):
#         """
#         API endpoint that allows Authnetification in the drive .
#         """
#         username = request.data['username']
#         password = request.data['password']

#         try:
#             # user = User.objects.get(username=username)
#             user = authenticate(username=username, password=password)
#         except user.DoesNotExist:
#             raise ValidationError('detail', 'unknown user')

#         if user is not None:
#             if user.is_active is False:
#                 # login(request, user)
#                 raise ValidationError('detail', 'Disabled account')
#             else:
#                 token = Token.objects.get_or_create(user=user)
#                 print(token.key)
#         else:
#             raise ValidationError('detail', 'unknown user')

#         message = {'origin': 'Server', 'user': username, 'code': 'Login'}

#         WsPublisher().ws_send(message)

#         return Response({'detail': token.__str__})

class RepositoryViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


class BatchViewSet(viewsets.ViewSet):
    url = r'Batchs'

    def list(self, request, username=None):
        pass


class DriveViewSet(viewsets.ViewSet):

    url = r'(?P<username>[-_\w]+)'

    _drive = Drive(settings.TREE_ROOT_NAME)

    # def list(self, request, username=None):
    #     """
    #     API endpoint that allows to get the user folders as Tree .
    #     """

    #     if username:

    #         if username == 'root':
    #             queryset = self._tree.buildTree()
    #         else:

    #             try:
    #                 User.objects.get(username=username)
    #             except User.DoesNotExist:
    #                 exc_type, exc_value, exc_traceback = sys.exc_info()
    # raise ValidationError('detail', 'invalid request data')
    #                 return Response(
    #                     {"status": "user does not exists : " + username},
    #                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #             queryset = self._tree.buildUserTree(username)

    #     serializer = TreeSerializer(queryset, many=True)
    #     return Response(serializer.data)

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

        queryset = self._drive.buildUserTree(pk)
        serializer = RepositoryNodeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, username):
        """
        API Create user root node.
        """
        root = self._drive.getRoot()
        pk = request.data['username']

        self._drive.createChild(root.id, pk, DriveConstants.get_default_type())

        queryset = self._drive.buildUserTree(pk)
        serializer = RepositoryNodeSerializer(queryset, many=True)

        return Response(serializer.data)


class DriveRepositoryViewSet(viewsets.ViewSet):

    url = r'(?P<username>[-_\w]+)/repositories'

    http_method_names = ['get', 'post', 'head', 'delete', 'put']

    _drive = Drive(settings.TREE_ROOT_NAME)

    def list(self, request, username):
        """
        API Get the Worspace the user .
        """
        # queryset = self._tree.buildUserTree(username, True)
        # serializer = TreeSerializer(queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        root = self._drive.getworkspace(username)
        return Response(RepositorySerializer(root).data,
                        status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def children(self, request, username, pk):
        """
        API Get all sub-repo of the repo.
        """
        queryset = self._drive.getChildren(pk)
        serializer = RepositorySerializer(queryset, many=True)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'])
    def files(self, request, username=None, pk=None):
        """
        API Get all documents of the repository.
        """
        queryset = File.objects.all()
        # folderId = self.request.query_params.get('id', None)
        if pk is not None:
            queryset = queryset.filter(repository_id=pk)

        paginator = LargeResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = FileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @detail_route(methods=['put'])
    def update(self, request, username, pk):
        """
        API Update libelle repository.
        """
        print(request.data)

        serializer = RepositorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('validated_data=' + json.dumps(serializer.validated_data))
            repository = Repository.objects.get(pk=pk)

            if repository is not None:

                repository.libelle = serializer.data['libelle']
                data_type = serializer.data['type']
                repository.type_id = data_type['id']

                repository.save()
                return Response(RepositorySerializer(repository).data,
                                status=status.HTTP_201_CREATED)
        else:
            raise ValidationError('invalid request data')

    def create(self, request, username):
        """
        API Create sub-repo of the repository.
        """
        serializer = CreateRepositorySerializer(data=request.data)
        if serializer.is_valid():

            parent = Repository.objects.get(pk=request.data['id'])

            if parent is None:
                raise ValidationError(
                    'invalid request data parent is none')

            else:

                folder = self._drive.createChild(
                    parent.id, serializer.data['libelle'],
                    DriveConstants.get_default_type())

                node = RepositoryNode(folder)

                return Response(RepositoryNodeSerializer(node).data,
                                status=status.HTTP_201_CREATED)
                # return Response(RepositorySerializer(folder).data,
                #            status=status.HTTP_201_CREATED)

        raise ValidationError('invalid request data')

    def destroy(self, request, username, pk=None):
        """ 
        API delete repository .
        """
        try:
            self._drive.remove(pk)
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


class DriveRepositoryAsTreeViewSet(viewsets.ViewSet):

    url = r'(?P<username>[-_\w]+)/tree'

    _drive = Drive(settings.TREE_ROOT_NAME)

    def list(self, request, username=None):
        """
        API Get all repositories of the user .
        """
        if username:

            if username == 'root':
                queryset = self._drive.buildTree()
            else:
                try:
                    User.objects.get(username=username)
                except User.DoesNotExist:
                    exc_type, exc_value, exc_traceback = sys.exc_info()

                    return Response(
                        {"status": "user does not exists : " + username},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                queryset = self._drive.buildUserTree(username)

        serializer = RepositoryNodeSerializer(queryset, many=True)
        return Response(serializer.data)


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
