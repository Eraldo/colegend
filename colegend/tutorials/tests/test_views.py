from django.core.urlresolvers import reverse
from django.test import TestCase
from lib.tests.test_views import LoggedInTestMixin, LoggedInManagerTestMixin
from tutorials.forms import TutorialForm
from tutorials.models import Tutorial
from tutorials.tests.test_models import TutorialFactory

__author__ = 'eraldo'


class TutorialListViewTest(LoggedInTestMixin, TestCase):
    def test_tutorial_list_view(self):
        tutorial = TutorialFactory()
        url = reverse("tutorials:tutorial_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(tutorial, response.context['object_list'])


class TutorialCreateViewTest(LoggedInManagerTestMixin, TestCase):
    def test_tutorial_new_view(self):
        url = reverse("tutorials:tutorial_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TutorialForm)

    def test_tutorial_new_view_saving_a_post_request(self):
        tutorial_attributes = TutorialFactory.attributes()
        tutorial_attributes["owner"] = self.manager
        url = reverse("tutorials:tutorial_new")
        response = self.client.post(url, data=tutorial_attributes)

        self.assertEqual(Tutorial.objects.count(), 1)
        new_tutorial = Tutorial.objects.first()
        self.assertEqual(new_tutorial.name, tutorial_attributes["name"])
        self.assertRedirects(response, reverse("tutorials:tutorial_list"))


class TutorialShowViewTest(LoggedInTestMixin, TestCase):
    def test_tutorial_show_view(self):
        tutorial = TutorialFactory()
        url = reverse("tutorials:tutorial_show", args=[tutorial.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tutorial, response.context['object'])


class TutorialEditViewTest(LoggedInManagerTestMixin, TestCase):
    def test_tutorial_edit_view(self):
        tutorial = TutorialFactory()
        url = reverse("tutorials:tutorial_edit", args=[tutorial.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TutorialForm)


class TutorialDeleteViewTest(LoggedInManagerTestMixin, TestCase):
    def test_tutorial_delete_view(self):
        tutorial = TutorialFactory()
        url = reverse("tutorials:tutorial_delete", args=[tutorial.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tutorial, response.context['object'])


class TutorialRedirectViewTest(LoggedInTestMixin, TestCase):
    def test_redirect_to_text_are_tutorial_view(self):
        tutorial = TutorialFactory(name="Text Areas")
        url = reverse("tutorials:text-areas")
        response = self.client.get(url, follow=True)

        self.assertRedirects(response, reverse("tutorials:tutorial_show", args=[tutorial.pk]))
        self.assertEqual(tutorial, response.context['object'])

    def test_redirect_to_not_existing_tutorial_view(self):
        url = reverse("tutorials:text-areas")
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 404)
