from django.test import TestCase
from .models import Task

__author__ = 'eraldo'


class TaskTests(TestCase):
    def setUp(self):
        Task.objects.create(name="write test")

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
