from django.test import TestCase
from users.models import User

__author__ = 'eraldo'


class UserManagerTests(TestCase):

    def test_create_user(self):
        manager = User.objects
        self.assertRaisesMessage(ValueError, "The given username must be set", manager.create_user, username=None)

    def test_create_superuser(self):
        manager = User.objects
        manager.create_superuser(username="manager", email="test@example.com", password="tester")
