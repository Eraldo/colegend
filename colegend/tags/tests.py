from django.test import TestCase
from tags.models import Tag
from users.models import User

__author__ = 'eraldo'


class TagModelTests(TestCase):

    def setUp(self):
        user_data = {
            "username": "Usernew", "password": "usernew",
        }
        self.user = User.objects.create(**user_data)

    def test_create_tag(self):
        tag_new = Tag.objects.create(name="tag1", owner=self.user)
        self.assertEqual(str(tag_new), "tag1")
