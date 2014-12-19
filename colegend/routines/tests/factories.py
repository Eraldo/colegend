import factory
from routines.models import Routine
from users.tests.factories import UserFactory

__author__ = 'eraldo'


class RoutineFactory(factory.DjangoModelFactory):
    class Meta:
        model = Routine
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Routine{0}'.format(n))
    description = "Some description."
    type = Routine.DEFAULT_TYPE
