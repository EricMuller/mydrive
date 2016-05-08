

from drive.models import UploadFile
from drive.serializers import UploadFileSerializer


from rest_framework import authentication
from rest_framework import generics
from rest_framework import permissions

from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from drive.consumers import WsPublisher
from json import dumps
import datetime


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


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        message = {'origin': 'Server', 'user': user.username,
                   'code': 'Login', 'date': str(datetime.datetime.now())}

        WsPublisher().ws_send('pong', message)

        return Response({'token': token.key})

obtain_auth_token = ObtainAuthToken.as_view()
