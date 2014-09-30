from django.contrib.auth import get_user_model
from django.core.exceptions import SuspiciousOperation, ValidationError
from django.test import TestCase
from projects.models import Project
from statuses.models import Status
from tasks.models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        user_cls = get_user_model()
        self.user = user_cls.objects.create_user(username="User", password="user")
        self.user2 = user_cls.objects.create_user(username="User2", password="user2")
        Status.objects.create(name="Status", order=1)
        self.project = Project.objects.create(name="Project", owner=self.user)

    def test_create_without_project(self):
        """
        Tests if a task can be created without a project.
        """
        task_new = Task.objects.create(name="Task", owner=self.user)
        task = Task.objects.get(name="Task")
        self.assertEqual(task_new, task)
        self.assertEqual(task.project, None)

    def test_create_with_project(self):
        """
        Tests if a task can be created with a project.
        """
        task = Task.objects.create(name="Task", project=self.project, owner=self.user)
        self.assertEqual(task.project, self.project)

    def test_create_task_for_foreign_project(self):
        """Make sure that a user cannot create a task that belongs to a foreign project."""
        project2 = Project.objects.create(name="Project2", owner=self.user2)
        self.assertRaises(
            SuspiciousOperation,
            Task.objects.create,
            name="Task", owner=self.user, project=project2
        )

    def test_duplicate_task_creation(self):
        """Make sure that creating a duplicate task with the same owner, project and name raises an exception."""
        task = Task.objects.create(name="Task", project=self.project, owner=self.user)
        self.assertRaises(
            ValidationError,
            Task.objects.create,
            name="Task", owner=self.user, project=self.project
        )

    def test_duplicate_task_creation_without_project(self):
        """Make sure that creating a duplicate task with the same owner, name and without a project raises an exception."""
        task = Task.objects.create(name="Task", owner=self.user)
        self.assertRaises(
            ValidationError,
            Task.objects.create,
            name="Task", owner=self.user
        )

