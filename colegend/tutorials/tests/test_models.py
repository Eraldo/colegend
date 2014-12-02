from django.test import TestCase
import factory
from tags.models import Tag
from tutorials.models import Tutorial, get_tutorial
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TutorialFactory(factory.DjangoModelFactory):

    class Meta:
        model = Tutorial
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Tutorial{0}'.format(n))
    description = "Some description."


class TutorialModelTests(TestCase):

    def setUp(self):
        self.user = TutorialFactory()

    def test_create_tutorial(self):
        tutorial_new = TutorialFactory()
        self.assertEqual(str(tutorial_new), tutorial_new.name)

    def test_get_tutorial(self):
        tutorial = TutorialFactory(name="foo")
        tutorial_fetched = get_tutorial("foo")

        self.assertEqual(tutorial_fetched, tutorial)
