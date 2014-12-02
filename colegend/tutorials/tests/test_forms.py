from django.test import TestCase
from tutorials.forms import TutorialForm
from tutorials.tests.test_models import TutorialFactory

__author__ = 'eraldo'


class TutorialFormTests(TestCase):

    def test_valid_form(self):
        data = TutorialFactory.attributes()
        form = TutorialForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        data = TutorialFactory.attributes()
        data["name"] = ""  # This should be invalid.
        form = TutorialForm(data=data)
        self.assertFalse(form.is_valid())
