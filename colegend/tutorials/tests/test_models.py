from django.test import TestCase
from tutorials.models import get_tutorial
from tutorials.tests.factories import TutorialFactory

__author__ = 'eraldo'


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
