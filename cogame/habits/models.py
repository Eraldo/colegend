from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import AutoUrlMixin, TrackedBase
from routines.models import Routine
from tags.models import TaggableBase

__author__ = 'eraldo'


class HabitQuerySet(QuerySet):
    pass


class HabitManager(PassThroughManagerMixin, models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Habit(AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a habit.
    """
    routine = models.ForeignKey(Routine, blank=True, null=True, related_name="habits")
    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    objects = HabitManager.for_queryset_class(HabitQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]
