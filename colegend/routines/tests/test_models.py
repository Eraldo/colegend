from django.test import TestCase
import factory
from routines.models import Routine
from statuses.tests.test_models import StatusFactory
from tasks.models import Task
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class RoutineFactory(factory.DjangoModelFactory):
    class Meta:
        model = Routine
        django_get_or_create = ('name',)

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'Routine{0}'.format(n))
    description = "Some description."
    type = Routine.DEFAULT_TYPE


class RoutineModelTests(TestCase):
    def test_create_routine(self):
        routine_new = RoutineFactory()
        self.assertEqual(str(routine_new), routine_new.name)
