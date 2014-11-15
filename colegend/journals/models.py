from django.db import models
from django.utils import timezone
from markitup.fields import MarkupField
from journals.validators import validate_present_or_past
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase, OwnedQueryMixin, ValidateModelMixin

__author__ = 'eraldo'


# class Journal(models.Model):
#     """
#     A django model representing a journal with an arbitrary number of entries per day.
#     """
#     pass

def get_last_location():
    return ""


class DayEntryQuerySet(OwnedQueryMixin, models.QuerySet):
    def latest_for(self, user):
        try:
            latest = self.owned_by(user).latest('date')
        except DayEntry.DoesNotExist:
            latest = None
        return latest

    def streak_for(self, user):
        entries = self.owned_by(user)
        dates = entries.dates('date', kind='day', order="DESC")
        today = timezone.datetime.today().date()
        # if not today in dates:
        #     return 0
        counter = 0
        for date in dates:
            if (today - date).days == counter:
                counter += 1
            else:
                return counter


class DayEntry(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a daily journal entry in text form.
    """
    # > owner: User
    date = models.DateField(default=timezone.datetime.today, validators=[validate_present_or_past])
    location = models.CharField(max_length=100)
    focus = models.CharField(max_length=100, help_text="What was the most important experience/topic on this day?")
    text = models.TextField()
    content = MarkupField()

    objects = DayEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date"]
        unique_together = ('owner', 'date')
        verbose_name_plural = "Day Entries"

    def __str__(self):
        return "{}".format(self.date)
