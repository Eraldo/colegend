from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import TrackedBase, AutoUrlMixin
from status.models import Status
from status.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectQuerySet(StatusQueryMixin, QuerySet):
    pass


class ProjectManager(PassThroughManagerMixin, models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Project(AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    deadline = models.DateField(blank=True, null=True)

    objects = ProjectManager.for_queryset_class(ProjectQuerySet)()

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]

