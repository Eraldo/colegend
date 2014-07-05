from django.db import models
from lib.models import TrackedBase, AutoUrlMixin
from status.models import Status, StatusManagerMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectManager(StatusManagerMixin, models.Manager):
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

    objects = ProjectManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]

