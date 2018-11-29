from django.contrib.auth.hashers import check_password
from django.test import TestCase

from ..serializers import UserSerializer


class TestUserSerializer(TestCase):
    """
    This class defines the test suite for the User serializer.
    """
    def setUp(self):
        """
        To set up the required data.
        """
        self.user_data = {'email': 'test@test.com', 'username': 'test122', 'password': '123', 'age': 12}

    def test_serializer_with_empty_data(self):
        """
        Tests the serializer's behaviour when empty data is passed.
        :rtype: bool
        """
        serializer = UserSerializer(data={})
        assert serializer.is_valid() == False

    def test_serializer_with_valid_data(self):
        """
        Tests the serializer's behaviour when data is passed.
        :rtype: bool
        """
        serializer = UserSerializer(data=self.user_data)
        assert serializer.is_valid()
