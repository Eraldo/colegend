from django.core.urlresolvers import reverse
from django.test import TestCase
from lib.tests.test_views import LoggedInTestMixin, LoggedInManagerTestMixin
from projects.forms import ProjectForm
from projects.models import Project
from projects.tests.test_models import ProjectFactory
from statuses.tests.test_models import StatusFactory

__author__ = 'eraldo'


class ProjectListViewTest(LoggedInTestMixin, TestCase):
    def test_project_list_view(self):
        project = ProjectFactory()
        url = reverse("projects:project_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(project, response.context['object_list'])


class ProjectNewViewTest(LoggedInTestMixin, TestCase):
    def test_project_new_view(self):
        url = reverse("projects:project_new")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ProjectForm)

    def test_project_new_view_saving_a_post_request(self):
        project_attributes = ProjectFactory.attributes()
        project_attributes["owner"] = self.user.pk
        project_attributes["status"] = StatusFactory().pk
        url = reverse("projects:project_new")
        response = self.client.post(url, data=project_attributes)

        self.assertEqual(Project.objects.count(), 1)
        new_project = Project.objects.first()
        self.assertEqual(new_project.name, project_attributes["name"])
        self.assertRedirects(response, reverse("projects:project_list"))

    def test_project_new_view_check_invalid_empty_post_request(self):
        url = reverse("projects:project_new")
        response = self.client.post(url, data=None)

        self.assertEqual(Project.objects.count(), 0)
        self.assertFormError(response, "form", "name", "This field is required.")
        self.assertFormError(response, "form", "status", "This field is required.")
        self.assertFormError(response, "form", "priority", "This field is required.")
        self.assertEqual(response.status_code, 200)

    def test_duplicate_owner_and_name(self):
        project_attributes = ProjectFactory.attributes()
        status = StatusFactory()
        project_attributes["owner"] = self.user
        project_attributes["status"] = status
        Project.objects.create(**project_attributes)
        project_attributes["owner"] = self.user.pk
        project_attributes["status"] = status.pk
        url = reverse("projects:project_new")
        response = self.client.post(url, data=project_attributes)

        self.assertFormError(response, 'form', None, 'Project with this Owner and Name already exists.')


class ProjectShowViewTest(LoggedInTestMixin, TestCase):
    def test_project_show_view(self):
        project = ProjectFactory()
        url = reverse("projects:project_show", args=[project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(project, response.context['object'])


class ProjectEditViewTest(LoggedInTestMixin, TestCase):
    def test_project_edit_view(self):
        project = ProjectFactory()
        url = reverse("projects:project_edit", args=[project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ProjectForm)


class ProjectDeleteViewTest(LoggedInTestMixin, TestCase):
    def test_project_delete_view(self):
        project = ProjectFactory()
        url = reverse("projects:project_delete", args=[project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(project, response.context['object'])
