from django.core.urlresolvers import reverse
from django.test import TestCase
from journals.forms import DayEntryForm
from lib.tests.test_views import LoggedInTestMixin

__author__ = 'eraldo'


class DayEntryDayEntryNewViewTest(LoggedInTestMixin, TestCase):
    def test_dayentry_new_view(self):
        url = reverse("journals:dayentry_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], DayEntryForm)

    def test_load_initial_custom_template_text(self):
        """
        Make sure that the custom journal entry template from the user settings
        get loaded as the initial text when creating a new journal entry.
        """
        # Setup: Define Journal Template.
        settings = self.user.settings
        template = "Some Template"
        settings.journal_entry_template = template
        settings.save()
        # Get page.
        url = reverse("journals:dayentry_new")
        response = self.client.get(url)

        # Check initial content.
        self.assertEqual(template, response.context["form"].initial.get("content"))
