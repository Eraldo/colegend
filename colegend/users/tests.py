import datetime
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.test import TestCase
from users.models import User


class UserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "Usernew", "email": "user_new@example.com", "password": "usernew",
            "birthday": datetime.date(2004, 4, 4),
            "phone_number": "+43123456789",
            "street": "NewStreet 4",
            "postal_code": "1234",
            "city": "Linz",
            "country": "Austria"
        }

    def test_user_creation(self):
        """Test the creation of a new user."""
        User.objects.create_user(**self.user_data)
        user = User.objects.get(username="Usernew")
        self.assertEquals(user.email, "user_new@example.com")
        self.assertEquals(user.country, "Austria")

    def test_username_taken(self):
        """Test the creation of a user with a username that is already taken."""
        User.objects.create_user(**self.user_data)
        self.assertRaises(
            IntegrityError,
            User.objects.create_user,
            self.user_data
        )

    def test_country_missing(self):
        """Test the creation of a user without the required country field."""
        User.objects.create_user(**self.user_data.pop("country"))
        self.assertRaises(
            IntegrityError,
            User.objects.create_user,
            self.user_data
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
