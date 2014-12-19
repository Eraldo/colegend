import factory
from projects.tests.factories import ProjectFactory
from statuses.tests.factories import StatusFactory
from tasks.models import Task
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class TaskFactory(factory.DjangoModelFactory):
    class Meta:
        model = Task
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
    name = factory.Sequence(lambda n: 'Task{0}'.format(n))
    description = "Some description."
    status = factory.SubFactory(StatusFactory)
    # date = ""
    # deadline = ""
