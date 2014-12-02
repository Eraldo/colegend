from django.core.exceptions import ValidationError
from django.test import TestCase
from users.validators import validate_checked

__author__ = 'eraldo'


class ValidatorTests(TestCase):

    def test_validate_checked(self):
        self.assertRaisesMessage(ValidationError, 'Needs to be checked.', validate_checked, value=False)
