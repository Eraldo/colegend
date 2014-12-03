from django.test import TestCase
from projects.forms import ProjectForm
from projects.tests.test_models import ProjectFactory

__author__ = 'eraldo'


class ProjectFormTests(TestCase):
    def test_valid_form(self):
        project = ProjectFactory()  # Creating owner and status obejects.
        data = ProjectFactory.attributes()
        data["owner"] = project.owner.pk
        data["status"] = project.status.pk
        form = ProjectForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        project = ProjectFactory()  # Creating owner and status obejects.
        data = ProjectFactory.attributes()
        data["owner"] = project.owner.pk
        data["status"] = project.status.pk
        data["name"] = ""  # Invalid! ;)
        form = ProjectForm(data=data)

        self.assertFalse(form.is_valid())
