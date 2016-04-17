
import sys
from drive import settings

from drive.mptt import TreeSerializer
from drive.mptt import Tree
# from drive.views import DefaultsAuthentificationMixin
from django.contrib.auth.models import User

from drive.models import Document
from drive.modules.drive import DriveNode
from drive.modules.drive import DriveNodeSerializer
from drive.serializers import DocumentSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class DriveNodeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DriveNode.objects.all()
    serializer_class = DriveNodeSerializer


class DriveViewSet(viewsets.ViewSet):

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

    def create(self, request):

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

            folder = self._tree.createChild(
                parent.id, serializer.data['libelle'])

            return Response(DriveNodeSerializer(folder).data,
                            status=status.HTTP_201_CREATED)

        raise ValidationError('detail', 'invalid request data')

    def destroy(self, request, username, pk=None):

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
