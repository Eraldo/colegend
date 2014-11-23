import datetime
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import TestCase
from users.models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "Usernew", "password": "usernew",
        }

    def test_user_creation(self):
        """Test the creation of a new user."""
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        self.assertEquals(user.check_password(self.user_data["password"]), True)

    def test_username_taken(self):
        """Test the creation of a user with a username that is already taken."""
        User.objects.create_user(**self.user_data)
        self.assertRaises(
            IntegrityError,
            User.objects.create_user,
            **self.user_data
        )

    def test_username_missing(self):
        """Test the creation of a user without the required username field."""
        data = self.user_data
        data.pop("username")
        self.assertRaises(
            TypeError,
            User.objects.create_user,
            **data
        )

    def test_password_missing(self):
        """Test the creation of a user without the password. A random password should be chosen."""
        data = self.user_data
        data.pop("password")
        User.objects.create_user(**data)
        user = User.objects.get(username="Usernew")
        self.assertEquals(len(user.password), 41)

    def test_get_name(self):
        """Test the retrieval of the user's name."""
        data = self.user_data
        data["first_name"] = "FirstName"
        data["last_name"] = "LastName"
        User.objects.create_user(**data)
        user = User.objects.get(username=data["username"])
        self.assertEquals(user.get_name(), "FirstName LastName")

    def test_is_accepted(self):
        """Test the user property: default, get, set."""
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        # Test getter
        self.assertIsNotNone(user.is_accepted)
        # Make sure that a new user is not accepted by default.
        self.assertFalse(user.is_accepted)
        # Test setter
        user.is_accepted = True
        self.assertTrue(user.is_accepted)

    def test_accept(self):
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        user.accept()

        # Check if the acceptance flag was set.
        self.assertTrue(user.is_accepted)

    def test_accept_email(self):
        from django.core import mail
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username=self.user_data["username"])
        user.accept()

        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, '[CoLegend] Account verified!')


class UserViewTests(TestCase):
    def test_list_view_anonymous(self):
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)

    def test_list_view_authenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=True)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Usernew")
        self.assertQuerysetEqual(response.context['user_list'], ['<User: Usernew>'])

    def test_list_view_unauthenticated(self):
        """Test the user list view with a logged in user."""
        usernew = User.objects.create_user(username="Usernew", password="usernew", is_accepted=False)
        self.client.login(username="Usernew", password="usernew")
        response = self.client.get(reverse('users:list'))
        self.assertEquals(response.status_code, 302)
