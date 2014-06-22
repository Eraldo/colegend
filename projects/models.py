from django.db import models
from lib.models import TrackedBase, AutoUrlMixin
from status.models import Status
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Project(AutoUrlMixin, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    objects = ProjectManager()

    name = models.CharField(max_length=200, unique=True)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.objects.default())
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]

