from rest_framework.test import APITestCase

from weight_management_api.users.models import User


class TestUserModelTestCase(APITestCase):
    """This class defines the test suite for the User model."""

    def setUp(self):
        """Define the test user and other test variables."""
        self.user = User(
            username='John92',
            email='john@test.com',
            age=23,
            password='123'
        )

    def test_create_client(self):
        """Test the user model can create a user."""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)
