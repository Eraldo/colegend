from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
from users.tests.test_models import UserFactory

__author__ = 'eraldo'


class ContactViewTests(TestCase):
    def test_get_contact_view_anonymous(self):
        eraldo = UserFactory(username="Eraldo", is_manager=True, first_name="Eraldo", last_name="Energy")
        url = reverse("contact")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eraldo Energy")

    def test_get_contact_view(self):
        eraldo = UserFactory(username="Eraldo", password="tester", is_manager=True, first_name="Eraldo", last_name="Energy")
        self.client.login(username=eraldo.username, password="tester")
        url = reverse("contact")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(eraldo, response.context['managers'])
        self.assertContains(response, "Eraldo Energy")

    def test_has_managers(self):
        UserFactory(username="Eraldo", password="tester", is_manager=True, first_name="Eraldo", last_name="Energy")
        url = reverse("contact")
        response = self.client.get(url)

        self.assertGreater(response.context['managers'].count(), 0)

    def test_send_message_anonymous(self):
        url = reverse("contact")
        data = {
            'email': 'tester@example.com',
            'message': 'test message',
        }
        response = self.client.post(url, data=data)

        # Check sent email message.
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, "[CoLegend] Message from '{}'".format(data.get("email")))
