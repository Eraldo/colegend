from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import TestCase
from users.models import User


class UserModelTests(TestCase):
    def test_user_creation(self):
        """Test the creation of a new user."""
        User.objects.create_user(username="Usernew", email="user_new@example.com", password="usernew")
        user = User.objects.get(username="Usernew")
        self.assertEquals(user.email, "user_new@example.com")

    def test_username_taken(self):
        """Test the creation of a user with a username that is already taken."""
        User.objects.create_user(username="Usernew", email="user_new@example.com", password="usernew")
        self.assertRaises(
            IntegrityError,
            User.objects.create_user,
            username="Usernew", email="user_new@example.com", password="usernew"
        )


class UserViewTests(TestCase):
    def test_list_view_anonymous(self):
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)

    def test_list_view_authenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew")
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Usernew")
        self.assertQuerysetEqual(response.context['user_list'], ['<User: Usernew>'])
