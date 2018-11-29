from django.contrib.auth.models import Group
from rest_framework import serializers

from weight_management_api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'age')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        model = Group
        fields = ('url', 'name')
