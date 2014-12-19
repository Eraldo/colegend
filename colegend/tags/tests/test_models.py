from django.test import TestCase
from tags.models import Tag
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TagModelTests(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_tag(self):
        tag_new = Tag.objects.create(name="tag1", owner=self.user)
        self.assertEqual(str(tag_new), "tag1")
