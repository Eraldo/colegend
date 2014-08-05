from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import AutoUrlMixin, TrackedBase, OwnedBase, OwnedQueryMixin
from routines.models import Routine
from tags.models import TaggableBase

__author__ = 'eraldo'


class HabitQuerySet(OwnedQueryMixin, QuerySet):
    pass


class HabitManager(PassThroughManagerMixin, models.Manager):
    pass


class Habit(AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a habit.
    """
    # > owner: User
    routine = models.ForeignKey(Routine, blank=True, null=True, related_name="habits")
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    objects = HabitManager.for_queryset_class(HabitQuerySet)()

    class Meta:
        ordering = ["name"]
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name
