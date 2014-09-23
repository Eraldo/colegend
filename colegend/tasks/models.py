from django.core.exceptions import ValidationError, SuspiciousOperation
from django.db import models
from django.db.models.query import QuerySet
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin, ValidateModelMixin
from projects.models import Project
from statuses.models import Status
from statuses.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class TaskQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class Task(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a task.
    """
    # > owner: User
    project = models.ForeignKey(Project, blank=True, null=True, related_name="tasks")
    name = models.CharField(max_length=100, help_text="Tip: Use a verb as the first word.")

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    priority = models.IntegerField(default=2)
    date = models.DateField(blank=True, null=True, help_text="When will I start?")
    deadline = models.DateField(blank=True, null=True)

    objects = TaskQuerySet.as_manager()

    class Meta:
        ordering = ["status", "priority", "project", "name"]
        unique_together = (('owner', 'project', 'name'),)

    def __str__(self):
        return self.name

    def clean(self):
        super(Task, self).clean()
        # Prevent duplicate names if the project was not set.
        if not self.project and Task.objects.filter(project__isnull=True, name=self.name).exists():
            raise ValidationError("A Task with this name and without a project exists already.")
        # Prevent the creation of a task for a project that is not owned.
        if self.project and not self.project.owner == self.owner:
            raise SuspiciousOperation("Cannot create a Task for a foreign project.")
