from django.test import TestCase
from routines.forms import RoutineForm
from routines.tests.test_models import RoutineFactory

__author__ = 'eraldo'


class RoutineFormTests(TestCase):
    def test_valid_form(self):
        routine = RoutineFactory()  # Creating owner and status obejects.
        data = RoutineFactory.attributes()
        data["owner"] = routine.owner.pk
        form = RoutineForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        routine = RoutineFactory()  # Creating owner and status obejects.
        data = RoutineFactory.attributes()
        data["owner"] = routine.owner.pk
        data["name"] = ""  # Invalid! ;)
        form = RoutineForm(data=data)

        self.assertFalse(form.is_valid())
