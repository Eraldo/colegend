from django.test import TestCase
import factory
from projects.models import Project
from statuses.models import Status
from statuses.tests.test_models import StatusFactory
from tasks.models import Task
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Project{0}'.format(n))
    description = "Some description."
    status = factory.SubFactory(StatusFactory)
    priority = 2
    # deadline = ""


class ProjectModelTests(TestCase):
    def test_create_project(self):
        project_new = ProjectFactory()
        self.assertEqual(str(project_new), project_new.name)

    def test_has_next_step(self):
        user = UserFactory()
        project = ProjectFactory()

        self.assertFalse(project.has_next_step)

        # TODO: Replace with TaskFactory
        Task.objects.create(owner=user, name="Task1", project=project, priority=1)

        self.assertTrue(project.has_next_step)
