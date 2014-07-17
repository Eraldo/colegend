from django.db import models
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase
from tags.models import TaggableBase

__author__ = 'eraldo'


class RoutineManager(models.Manager):
    def owned_by(self, user):
        return self.filter(owner=user)


class Routine(AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a routine.
    """
    # > owner: User
    name = models.CharField(max_length=100)

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
        unique_together = (('owner', 'name'),)

    def __str__(self):
        return self.name
