from django.core import mail
from django.test import TestCase
from contact.forms import ContactForm, PublicContactForm
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class ContactFormTests(TestCase):
    def test_valid_form(self):
        data = {
            'message': 'test message',
        }
        form = ContactForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_with_blank_message(self):
        data = {
            'message': '',
        }
        form = ContactForm(data=data)

        self.assertFalse(form.is_valid())

    def test_send_email(self):
        user = UserFactory()
        data = {
            'message': 'test message',
        }
        form = ContactForm(data=data)
        form.is_valid()
        form.send_email(user)

        # Check sent email message.
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, "[CoLegend] Message from '{}'".format(user))


class PublicContactFormTests(TestCase):
    def test_valid_form(self):
        data = {
            'email': 'tester@example.com',
            'message': 'test message',
        }
        form = PublicContactForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form_with_invalid_email(self):
        data = {
            'email': 'hello',
            'message': 'test message',
        }
        form = PublicContactForm(data=data)

        self.assertFalse(form.is_valid())

    def test_send_email(self):
        data = {
            'email': 'tester@example.com',
            'message': 'test message',
        }
        form = PublicContactForm(data=data)
        form.is_valid()
        form.send_email()

        # Check sent email message.
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, "[CoLegend] Message from '{}'".format(data.get("email")))
