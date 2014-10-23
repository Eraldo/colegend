from django.db import models
from django.db.models.query import QuerySet
from lib.models import AutoUrlMixin, TrackedBase, OwnedBase, OwnedQueryMixin, ValidateModelMixin
from routines.models import Routine
from tags.models import TaggableBase

__author__ = 'eraldo'


class HabitQuerySet(OwnedQueryMixin, QuerySet):
    pass


class Habit(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a habit.
    """
    # > owner: User
    routine = models.ForeignKey(Routine, blank=True, null=True, related_name="habits")
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField()

    objects = HabitQuerySet.as_manager()

    class Meta:
        ordering = ["order", "name"]
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name
