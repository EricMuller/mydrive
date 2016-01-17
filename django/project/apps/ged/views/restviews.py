import datetime

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from ged.models import Basket
from ged.models import Document
from ged.models import UploadFile


from ged.serializers import UserSerializer
from ged.serializers import GroupSerializer
from ged.serializers import BasketSerializer
from ged.serializers import DocumentSerializer
from ged.serializers import UploadFileSerializer


from rest_framework import authentication
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route

from rest_framework.response import Response


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


class BasketViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (permissions.AllowAny,)

    @list_route(methods=['get', ])
    def code(self, request, pk=None):

        snippet = "code"
        return Response(snippet)

    @detail_route(methods=['get', ])
    def accounts(self, request, pk):

        snippet = "Highlight"
        return Response(snippet)
pass


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
