from django.core.urlresolvers import reverse
from django.test import TestCase
import factory
from tags.models import Tag
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TagFactory(factory.DjangoModelFactory):

    class Meta:
        model = Tag
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Tag{0}'.format(n))
    description = "Some description."


class TagModelTests(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_tag(self):
        tag_new = Tag.objects.create(name="tag1", owner=self.user)
        self.assertEqual(str(tag_new), "tag1")
