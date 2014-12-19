from django.test import TestCase
from statuses.models import Status
from statuses.tests.factories import StatusFactory

__author__ = 'eraldo'


class StatusModelTests(TestCase):
    def test_create_status(self):
        status_new = StatusFactory()
        self.assertEqual(str(status_new), status_new.name)


class StatusManagerModelTest(TestCase):
    def test_open(self):
        open1 = StatusFactory(name="open1", type=Status.OPEN)
        open2 = StatusFactory(name="open2", type=Status.OPEN)
        closed1 = StatusFactory(name="closed1", type=Status.CLOSED)
        closed2 = StatusFactory(name="closed2", type=Status.CLOSED)

        self.assertIn(open1, Status.objects.open())
        self.assertIn(open2, Status.objects.open())
        self.assertNotIn(closed1, Status.objects.open())
        self.assertNotIn(closed2, Status.objects.open())

    def test_closed(self):
        open1 = StatusFactory(name="open1", type=Status.OPEN)
        open2 = StatusFactory(name="open2", type=Status.OPEN)
        closed1 = StatusFactory(name="closed1", type=Status.CLOSED)
        closed2 = StatusFactory(name="closed2", type=Status.CLOSED)

        self.assertNotIn(open1, Status.objects.closed())
        self.assertNotIn(open2, Status.objects.closed())
        self.assertIn(closed1, Status.objects.closed())
        self.assertIn(closed2, Status.objects.closed())
