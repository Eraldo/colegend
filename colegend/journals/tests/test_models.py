from django.test import TestCase
from django.utils import timezone
from journals.models import DayEntry
from lib.tests.test_views import LoggedInTestMixin

__author__ = 'eraldo'


class DayEntryDayEntryNewViewTest(LoggedInTestMixin, TestCase):

    def get_dayentry_streak(self):
        return DayEntry.objects.streak_for(self.user)

    def test_empty_dayentry_streak(self):
        user = self.user
        self.assertEqual(0, self.get_dayentry_streak())

    def test_continuous_dayentry_streak(self):
        user = self.user
        today = timezone.now().date()
        DayEntry.objects.bulk_create([
            DayEntry(journal=user.journal, date=today),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(1)),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(2)),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(3)),
        ])
        self.assertEqual(4, self.get_dayentry_streak())

    def test_continuous_dayentry_streak_without_today(self):
        user = self.user
        today = timezone.now().date()
        DayEntry.objects.bulk_create([
            DayEntry(journal=user.journal, date=today - timezone.timedelta(1)),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(2)),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(3)),
        ])
        self.assertEqual(3, self.get_dayentry_streak())

    def test_broken_dayentry_streak(self):
        user = self.user
        today = timezone.now().date()
        DayEntry.objects.bulk_create([
            DayEntry(journal=user.journal, date=today),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(1)),
            DayEntry(journal=user.journal, date=today - timezone.timedelta(3)),
        ])
        self.assertEqual(2, self.get_dayentry_streak())
