from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin
from projects.models import Project
from status.models import Status
from status.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class TaskQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class TaskManager(PassThroughManagerMixin, models.Manager):
    pass


class Task(AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a task.
    """
    # > owner: User
    project = models.ForeignKey(Project, blank=True, null=True, related_name="tasks")
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    objects = TaskManager.for_queryset_class(TaskQuerySet)()

    class Meta:
        ordering = ["project", "name"]
        unique_together = (('owner', 'project', 'name'),)

    def __str__(self):
        return self.name
