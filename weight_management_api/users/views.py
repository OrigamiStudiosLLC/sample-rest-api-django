from django.contrib.auth.models import Group
from django.db import IntegrityError
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from weight_management_api.users.models import User
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created, viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new user in the system.
        :param request: HTTP request.
        :param args: list arguments
        :param kwargs: dict key word arguments
        :return: HTTP response with token.
        """
        try:
            serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            user = User(
                username=validated_data.get('username'),
                email=validated_data.get('email'),
                age=validated_data.get('age')
            )
            user.set_password(validated_data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            return Response(data={'authentication_token': token.key}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            raise e


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Logout(APIView):
    """
    API endpoint that expires user's authentication token.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Deletes the authentication token.
        :param request: HTTP request.
        :return: HTTP response.
        """
        request.user.auth_token.delete()
        return Response(
            data={'Message': 'Token has successfully expired.'},
            status=status.HTTP_200_OK
        )
