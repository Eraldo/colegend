from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import AutoUrlMixin, TrackedBase, OwnedBase
from routines.models import Routine
from tags.models import TaggableBase

__author__ = 'eraldo'


class HabitQuerySet(QuerySet):
    pass


class HabitManager(PassThroughManagerMixin, models.Manager):
    def get_by_natural_key(self, owner, routine, name):
        return self.get(owner=owner, routine=routine, name=name)


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
        unique_together = (('owner', 'routine', 'name'),)

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.owner.natural_key(), self.routine.natural_key(), self.name]

    natural_key.dependencies = ['users.user', 'routines.routine']
