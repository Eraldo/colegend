from django.test import TestCase
from projects.tests.factories import ProjectFactory
from statuses.tests.factories import StatusFactory
from tasks.tests.factories import TaskFactory
from users.tests.factories import UserFactory

__author__ = 'eraldo'


class ProjectModelTests(TestCase):
    def test_create_project(self):
        project_new = ProjectFactory()
        self.assertEqual(str(project_new), project_new.name)

    def test_has_next_step(self):
        user = UserFactory()
        project = ProjectFactory()

        self.assertFalse(project.has_next_step)

        TaskFactory(owner=user, name="task1", project=project, status=StatusFactory(name="next"))

        self.assertTrue(project.has_next_step)
