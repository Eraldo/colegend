from django.test import TestCase
from tags.forms import TagForm
from tags.tests.test_models import TagFactory

__author__ = 'eraldo'


class TagFormTests(TestCase):

    def test_valid_form(self):
        data = TagFactory.attributes()
        form = TagForm(data=data)
        self.assertTrue(form.is_valid())
