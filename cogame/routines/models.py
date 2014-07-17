from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class RoutineQuerySet(OwnedQueryMixin, QuerySet):
    pass


class RoutineManager(PassThroughManagerMixin, models.Manager):
    pass


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

    objects = RoutineManager.for_queryset_class(RoutineQuerySet)()

    class Meta:
        ordering = ["name"]
        unique_together = (('owner', 'name'),)

    def __str__(self):
        return self.name
