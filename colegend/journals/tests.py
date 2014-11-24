from unittest import skip
from django.test import TestCase

__author__ = 'eraldo'


class DayEntryModelTest(TestCase):
    def setUp(self):
        pass

    @skip("TODO: fix")
    def test_load_initial_custom_template_text(self):
        """
        Make sure that the custom journal entry template from the user settings
        get loaded as the initial text when creating a new journal entry.
        """
        self.fail("TODO: Write test.")
