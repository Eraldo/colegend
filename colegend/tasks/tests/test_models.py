from django.core.exceptions import SuspiciousOperation, ValidationError
from django.test import TestCase
from projects.tests.test_models import ProjectFactory
from tasks.models import Task
from tasks.tests.factories import TaskFactory
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TaskModelTests(TestCase):
    def test_create_task(self):
        task_new = TaskFactory()

        self.assertEqual(str(task_new), task_new.name)

    def test_create_without_project(self):
        """
        Tests if a task can be created without a project.
        """
        task_new = TaskFactory(project=None)
        task = Task.objects.get(name=task_new.name)

        self.assertEqual(task_new, task)
        self.assertEqual(task.project, None)

    def test_create_with_project(self):
        """
        Tests if a task can be created with a project.
        """
        project = ProjectFactory()
        task = TaskFactory(project=project)
        self.assertEqual(task.project, project)

    def test_create_task_for_foreign_project(self):
        """Make sure that a user cannot create a task that belongs to a foreign project."""
        user = UserFactory()
        other_user = UserFactory(username="otheruser")
        foreign_project = ProjectFactory(owner=other_user)

        self.assertRaises(
            SuspiciousOperation,
            Task.objects.create,
            name="SuspiciousTask", owner=user, project=foreign_project
        )

    def test_task_creation_with_duplicate_owner_project_and_name(self):
        """Make sure that creating a duplicate task with the same owner, project and name raises an exception."""
        project = ProjectFactory()
        task = Task.objects.create(name="Task", project=project, owner=project.owner)
        self.assertRaisesMessage(
            ValidationError,
            "Task with this Owner, Project and Name already exists.",
            Task.objects.create,
            name="Task", owner=project.owner, project=project
        )
