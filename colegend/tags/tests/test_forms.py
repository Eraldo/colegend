from django.test import TestCase
from tags.forms import TagForm
from tags.tests.factories import TagFactory

__author__ = 'eraldo'


class TagFormTests(TestCase):

    def test_valid_form(self):
        data = TagFactory.attributes()
        form = TagForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        data = TagFactory.attributes()
        data["name"] = ""  # This should be invalid.
        form = TagForm(data=data)
        self.assertFalse(form.is_valid())
