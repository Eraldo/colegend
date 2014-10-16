from django.db import models
from django.utils import timezone
from journals.validators import validate_present_or_past
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase, OwnedQueryMixin, ValidateModelMixin

__author__ = 'eraldo'


# class Journal(models.Model):
#     """
#     A django model representing a journal with an arbitrary number of entries per day.
#     """
#     pass


class DayEntryQuerySet(OwnedQueryMixin, models.QuerySet):
    pass


def get_last_location():
    try:
        return DayEntry.objects.latest('date').location
    except DayEntry.DoesNotExist:
        return ""


class DayEntry(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a daily journal entry in text form.
    """
    # > owner: User
    date = models.DateField(default=timezone.datetime.today, validators=[validate_present_or_past])
    text = models.TextField()

    location = models.CharField(max_length=100, default=get_last_location)

    objects = DayEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date"]
        unique_together = ('owner', 'date')
        verbose_name_plural = "Day Entries"

    def __str__(self):
        return "{}".format(self.date)
