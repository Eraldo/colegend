from django.test import TestCase
from tasks.forms import TaskForm
from tasks.tests.test_models import TaskFactory

__author__ = 'eraldo'


class TaskFormTests(TestCase):
    def test_valid_form(self):
        task = TaskFactory()  # Creating owner and status obejects.
        data = TaskFactory.attributes()
        data["owner"] = task.owner.pk
        data["project"] = task.project.pk
        data["status"] = task.status.pk
        form = TaskForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        task = TaskFactory()  # Creating owner and status obejects.
        data = TaskFactory.attributes()
        data["owner"] = task.owner.pk
        data["project"] = task.project.pk
        data["status"] = task.status.pk
        data["name"] = ""  # Invalid! ;)
        form = TaskForm(data=data)

        self.assertFalse(form.is_valid())
