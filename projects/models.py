from django.db import models
from lib.models import TrackedBase, TaggableBase
from status.models import Status

__author__ = 'eraldo'


class Project(TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    name = models.CharField(max_length=200, unique=True)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.objects.default())

    def __str__(self):
        return self.name