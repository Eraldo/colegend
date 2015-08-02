from django.db import models
from django.utils import timezone
from markitup.fields import MarkupField
from journals.validators import validate_present_or_past
from lib.models import AutoUrlMixin, TrackedBase, OwnedQueryMixin, ValidateModelMixin, AutoOwnedBase
from tags.models import TaggableBase

__author__ = 'eraldo'


class JournalQuerySet(OwnedQueryMixin, models.QuerySet):
    pass


class Journal(AutoOwnedBase, models.Model):
    """
    A django model representing a journal with one entry per day.
    """
    # > owner (pk)
    # > entries
    topic_of_the_year = models.CharField(max_length=100, blank=True)
    template = models.TextField(
        blank=True,
        help_text="The default text to be used as a basis when creating a new journal entry.")
    max_streak = models.IntegerField(default=0)
    max_week_streak = models.IntegerField(default=0)

    objects = JournalQuerySet.as_manager()

    def __str__(self):
        return "{}'s Journal".format(self.owner)

    @property
    def streak(self):
        return DayEntry.objects.streak_for(self.owner)


class DayEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)

    def latest_for(self, user):
        try:
            latest = self.owned_by(user).latest('date')
        except DayEntry.DoesNotExist:
            latest = None
        return latest

    def streak_for(self, user):
        entries = self.owned_by(user)
        dates = entries.dates('date', kind='day', order="DESC")
        today = timezone.now().date()
        counter = 0
        for date in dates:
            if (today - date).days == counter:
                counter += 1
            else:
                return counter
        # no dates found..
        return counter


class DayEntry(ValidateModelMixin, AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a daily journal entry in text form.
    """
    journal = models.ForeignKey(Journal, related_name="entries")
    date = models.DateField(default=timezone.datetime.today, validators=[validate_present_or_past])
    location = models.CharField(max_length=100)
    focus = models.CharField(max_length=100, help_text="What was the most important experience/topic on this day?")
    content = MarkupField()

    objects = DayEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date"]
        unique_together = ('journal', 'date')
        verbose_name_plural = "Day Entries"
        default_related_name = "day_entries"

    def __str__(self):
        return "{}".format(self.date)

    def update_streak(self):
        streak = DayEntry.objects.streak_for(self.journal.owner)
        if streak > self.journal.max_streak:
            self.journal.max_streak = streak
            self.journal.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_streak()

    def get_previous(self):
        return self.journal.entries.filter(date__lt=self.date).first()

    def get_next(self):
        return self.journal.entries.filter(date__gt=self.date).last()


class WeekEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)

    def latest_for(self, user):
        try:
            latest = self.owned_by(user).latest('date')
        except WeekEntry.DoesNotExist:
            latest = None
        return latest

    def streak_for(self, user):
        entries = self.owned_by(user)
        dates = entries.dates('date', kind='day', order="DESC")
        today = timezone.now().date()
        current_monday = today - timezone.timedelta(days=today.weekday())
        counter = 0
        for date in dates:
            monday = date - timezone.timedelta(days=date.weekday())
            if (current_monday - monday).days == counter * 7:
                counter += 1
            else:
                return counter
        # no dates found..
        return counter


class WeekEntry(ValidateModelMixin, AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a weekly journal entry in text form.
    """
    journal = models.ForeignKey(Journal, related_name="week_entries")
    date = models.DateField(default=timezone.datetime.today, validators=[validate_present_or_past])
    focus = models.CharField(max_length=100, help_text="What was the most important experience/topic on this week?")
    content = MarkupField()

    objects = WeekEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date"]
        unique_together = ('journal', 'date')
        verbose_name_plural = "Week Entries"
        default_related_name = "week_entries"

    def __str__(self):
        return "{}".format(self.date)

    def update_streak(self):
        streak = WeekEntry.objects.streak_for(self.journal.owner)
        if streak > self.journal.max_week_streak:
            self.journal.max_week_streak = streak
            self.journal.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_streak()

    def get_previous(self):
        return self.journal.entries.filter(date__lt=self.date).first()

    def get_next(self):
        return self.journal.entries.filter(date__gt=self.date).last()

    def get_first_day(self):
        return self.date - timezone.timedelta(days=self.date.weekday())
