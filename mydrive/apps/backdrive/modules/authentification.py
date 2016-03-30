
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session

from rest_framework import viewsets
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class AuthentificationViewSet(viewsets.ViewSet):

    def list(self, request):

        Session.objects.all().delete()
        # raise ValidationError({'detail': 'not implemented yet'})

        return Response({'detail': 'connected'},
                        status=status.HTTP_201_CREATED)

    def create(self, request):

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
