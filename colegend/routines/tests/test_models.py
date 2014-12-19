from django.test import TestCase
from routines.tests.factories import RoutineFactory

__author__ = 'eraldo'


class RoutineModelTests(TestCase):
    def test_create_routine(self):
        routine_new = RoutineFactory()
        self.assertEqual(str(routine_new), routine_new.name)
