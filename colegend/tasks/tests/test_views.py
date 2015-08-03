from django.core.urlresolvers import reverse
from django.test import TestCase
from lib.tests.test_views import LoggedInTestMixin
from tasks.forms import TaskForm
from tasks.models import Task
from tasks.tests.test_models import TaskFactory
from statuses.tests.test_models import StatusFactory

__author__ = 'eraldo'


class TaskListViewTest(LoggedInTestMixin, TestCase):
    def test_task_list_view(self):
        task = TaskFactory()
        url = reverse("tasks:task_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(task, response.context['object_list'])


class TaskNewViewTest(LoggedInTestMixin, TestCase):
    def test_task_new_view(self):
        url = reverse("tasks:task_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TaskForm)

    def test_task_new_view_saving_a_post_request(self):
        # data = TaskFactory.attributes()
        # Workaround for https://github.com/rbarrois/factory_boy/issues/198
        data = {
            "owner": self.user.pk,
            "name": "Task1",
            "status": StatusFactory().pk,
        }
        url = reverse("tasks:task_new")
        response = self.client.post(url, data=data)
        print(Task.objects.count())
        self.assertEqual(Task.objects.count(), 1)
        new_task = Task.objects.first()
        self.assertEqual(new_task.name, data["name"])
        self.assertRedirects(response, new_task.get_show_url())

    def test_task_new_view_check_invalid_empty_post_request(self):
        url = reverse("tasks:task_new")
        response = self.client.post(url, data=None)

        self.assertEqual(Task.objects.count(), 0)
        self.assertFormError(response, "form", "name", "This field is required.")
        self.assertFormError(response, "form", "status", "This field is required.")
        self.assertEqual(response.status_code, 200)

    def test_duplicate_owner_project_and_name(self):
        task = TaskFactory(owner=self.user, project__owner=self.user)
        # data = TaskFactory.attributes()
        # Workaround for https://github.com/rbarrois/factory_boy/issues/198
        data = {
            "owner": task.owner.pk,
            "project": task.project.pk,
            "name": task.name,
            "description": TaskFactory.description,
            "status": task.status.pk,
        }
        url = reverse("tasks:task_new")
        response = self.client.post(url, data=data)

        self.assertFormError(response, 'form', None, 'Task with this Owner, Project and Name already exists.')


class TaskShowViewTest(LoggedInTestMixin, TestCase):
    def test_task_show_view(self):
        task = TaskFactory()
        url = reverse("tasks:task_show", args=[task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(task, response.context['object'])


class TaskEditViewTest(LoggedInTestMixin, TestCase):
    def test_task_edit_view(self):
        task = TaskFactory()
        url = reverse("tasks:task_edit", args=[task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], TaskForm)


class TaskDeleteViewTest(LoggedInTestMixin, TestCase):
    def test_task_delete_view(self):
        task = TaskFactory()
        url = reverse("tasks:task_delete", args=[task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(task, response.context['object'])
