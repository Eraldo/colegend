from django.db import models
from lib.models import TrackedBase, AutoUrlMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class RoutineManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Routine(AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a routine.
    """
    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    DEFAULT = DAILY
    TYPES = (
        (DAILY, "daily"),
        (WEEKLY, "weekly"),
        (MONTHLY, "monthly"),
        (YEARLY, "yearly"),
    )
    type = models.CharField(default=DEFAULT, max_length=50, choices=TYPES)

    objects = RoutineManager()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]
