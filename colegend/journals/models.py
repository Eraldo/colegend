from django.db import models
from django.utils import timezone
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase, OwnedQueryMixin, ValidateModelMixin

__author__ = 'eraldo'


# class Journal(models.Model):
#     """
#     A django model representing a journal with an arbitrary number of entries per day.
#     """
#     pass


class DayEntryQuerySet(OwnedQueryMixin, models.QuerySet):
    pass


class DayEntry(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a daily journal entry in text form.
    """
    # > owner: User
    date = models.DateField(default=timezone.datetime.today)
    text = models.TextField()

    objects = DayEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date"]
        unique_together = ('owner', 'date')
        verbose_name_plural = "Day Entries"

    def __str__(self):
        return "{}".format(self.date)
