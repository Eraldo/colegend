import factory
from projects.models import Project
from users.tests.factories import UserFactory
from statuses.tests.factories import StatusFactory

__author__ = 'eraldo'


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Project{0}'.format(n))
    description = "Some description."
    status = factory.SubFactory(StatusFactory)
    # deadline = ""
