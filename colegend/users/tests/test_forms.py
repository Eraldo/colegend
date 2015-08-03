from django.test import TestCase
from users.forms import UserForm, UserCreationForm, SignUpApplicationForm
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class UserFormTests(TestCase):
    def test_valid_form(self):
        data = UserFactory.attributes()
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_name(self):
        data = UserFactory.attributes()
        data["username"] = ""  # This should be invalid.
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())


class UserCreationFormTests(TestCase):
    def test_valid_form(self):
        data = {
            "username": "johndoe",
            "password1": "tester",
            "password2": "tester",
        }
        form = UserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_username(self):
        data = {
            "username": "",  # This should be invalid.
            "password1": "tester",
            "password2": "tester",
        }
        form = UserCreationForm(data=data)
        self.assertFalse(form.is_valid())


class SignUpApplicationFormTests(TestCase):
    def test_valid_form(self):
        # data = {}
        # contact_data = ContactFactory.attributes()
        # data.update(contact_data)
        # profile_data = ProfileFactory.attributes()
        # data.update(profile_data)
        # print(data)
        data = {
            'username': 'johndoe',

            'origin': 'some origin',
            'referrer': 'some referrer',
            'experience': 'some experience',
            'motivation': 'some motivation',
            'change': 'some change',
            'drive': '4',
            'expectations': 'some expectations',
            'other': 'some other',

            'stop': 'on',
            'discretion': 'on',
            'responsibility': 'on',
            'appreciation': 'on',
            'terms': 'on',

            "first_name": "John",
            "last_name": "Doe",
            "gender": "M",
            "birthday": "1900-01-01",
            "email": "johndoe@example.com",
            "phone_number": "+4369910203039",
            "street": "Street 1",
            "postal_code": "12345",
            "city": "Linz",
            "country": "Austria",

            'password1': 'tester',
            'password2': 'tester',

            'confirmation_key': '',
            'next': '/',
            'save': 'Send Application',
        }
        form = SignUpApplicationForm(data=data, initial={"username": "johndoe"})
        form.is_valid()
        self.assertTrue(form.is_valid())

    def test_invalid_form_without_data(self):
        data = UserFactory.attributes()
        data["username"] = ""  # This should be invalid.
        form = SignUpApplicationForm(data={})
        self.assertFalse(form.is_valid())

