from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestUserTestCase(APITestCase):
    """
    Tests /users operations.
    """

    def setUp(self):
        """
        To set up the required data.
        """
        self.url = '/api/v1/users/'
        self.user_data = {'email': 'test@test.com', 'username': 'mjh', 'password': '123', 'age': 12}

    def test_post_request_with_no_data_fails(self):
        """
        Tests the user creation endpoint with empty data.
        :rtype: bool
        """
        response = self.client.post(self.url, {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_request_with_valid_data_succeeds(self):
        """
        Tests the user creation endpoint with valid data.
        :rtype: bool
        """
        response = self.client.post(self.url, self.user_data)
        assert response.status_code == status.HTTP_201_CREATED

        user = Token.objects.get(key=response.data.get('authentication_token')).user
        assert user.username == self.user_data.get('username')
        assert check_password(self.user_data.get('password'), user.password)
