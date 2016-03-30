

from backdrive.models import UploadFile
from backdrive.serializers import UploadFileSerializer


from rest_framework import authentication
from rest_framework import generics
from rest_framework import permissions


class DefaultsAuthentificationMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.TokenAuthentication,
        authentication.BasicAuthentication
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SnippetList(generics.ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer
