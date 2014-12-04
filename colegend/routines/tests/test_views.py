from django.core.urlresolvers import reverse
from django.test import TestCase
from lib.tests.test_views import LoggedInTestMixin
from routines.forms import RoutineForm
from routines.models import Routine
from routines.tests.test_models import RoutineFactory
from statuses.tests.test_models import StatusFactory

__author__ = 'eraldo'


class RoutineListViewTest(LoggedInTestMixin, TestCase):
    def test_routine_list_view(self):
        routine = RoutineFactory()
        url = reverse("routines:routine_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(routine, response.context['object_list'])


class RoutineNewViewTest(LoggedInTestMixin, TestCase):
    def test_routine_new_view(self):
        url = reverse("routines:routine_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], RoutineForm)

    def test_routine_new_view_saving_a_post_request(self):
        routine_attributes = RoutineFactory.attributes()
        routine_attributes["owner"] = self.user.pk
        routine_attributes["status"] = StatusFactory().pk
        url = reverse("routines:routine_new")
        response = self.client.post(url, data=routine_attributes)

        self.assertEqual(Routine.objects.count(), 1)
        new_routine = Routine.objects.first()
        self.assertEqual(new_routine.name, routine_attributes["name"])
        self.assertRedirects(response, reverse("routines:routine_list"))

    def test_routine_new_view_check_invalid_empty_post_request(self):
        url = reverse("routines:routine_new")
        response = self.client.post(url, data=None)

        self.assertEqual(Routine.objects.count(), 0)
        self.assertFormError(response, "form", "name", "This field is required.")
        self.assertEqual(response.status_code, 200)

    def test_duplicate_owner_and_name(self):
        routine_attributes = RoutineFactory.attributes()
        status = StatusFactory()
        routine_attributes["owner"] = self.user
        Routine.objects.create(**routine_attributes)
        routine_attributes["owner"] = self.user.pk
        url = reverse("routines:routine_new")
        response = self.client.post(url, data=routine_attributes)

        self.assertFormError(response, 'form', None, 'Routine with this Owner and Name already exists.')


class RoutineShowViewTest(LoggedInTestMixin, TestCase):
    def test_routine_show_view(self):
        routine = RoutineFactory()
        url = reverse("routines:routine_show", args=[routine.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(routine, response.context['object'])


class RoutineEditViewTest(LoggedInTestMixin, TestCase):
    def test_routine_edit_view(self):
        routine = RoutineFactory()
        url = reverse("routines:routine_edit", args=[routine.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], RoutineForm)


class RoutineDeleteViewTest(LoggedInTestMixin, TestCase):
    def test_routine_delete_view(self):
        routine = RoutineFactory()
        url = reverse("routines:routine_delete", args=[routine.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(routine, response.context['object'])
