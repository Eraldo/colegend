from django.db import models
from lib.models import TrackedBase, TaggableBase
from projects.models import Project
from status.models import Status

__author__ = 'eraldo'


class Task(TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a task.
    """
    project = models.ForeignKey(Project, blank=True, null=True, related_name="tasks")
    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.objects.default())
    date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["project", "name"]

    def __str__(self):
        return self.name
