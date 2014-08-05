from django.test import TestCase
from projects.models import Project
from tasks.models import Task


__author__ = 'eraldo'


class TaskTests(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(name="p1")
        Task.objects.create(name="do a")
        Task.objects.create(name="do b")

    def test_create_without_project(self):
        """
        Tests if a task can be created without a project.
        """
        task = Task.objects.create(name="do c")
        self.assertEqual(task.project, None)

    def test_create_with_project(self):
        """
        Tests if a task can be created with a project.
        """

        task = Task.objects.create(name="do d", project=self.project1)
        self.assertEqual(task.project, self.project1)

