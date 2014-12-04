from django.core.exceptions import ValidationError, SuspiciousOperation
from django.db import models
from django.db.models.query import QuerySet
from markitup.fields import MarkupField
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin, ValidateModelMixin
from projects.models import Project
from statuses.models import Status
from statuses.utils import StatusQueryMixin
from tags.models import TaggableBase
from users.models import User

__author__ = 'eraldo'


class TaskQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    def open(self):
        return self.filter(status__type=Status.OPEN)

    def closed(self):
        return self.filter(status__type=Status.CLOSED)


class Task(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a task.
    """
    # > owner: User
    project = models.ForeignKey(Project, blank=True, null=True, related_name="tasks")
    name = models.CharField(max_length=100, help_text="Tip: Use a verb as the first word.")

    description = MarkupField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    priority = models.IntegerField(default=2)
    date = models.DateField(blank=True, null=True, help_text="When will I start?")
    deadline = models.DateField(blank=True, null=True)

    objects = TaskQuerySet.as_manager()

    class Meta:
        ordering = ["status", "priority", "project", "name"]
        unique_together = ('owner', 'project', 'name')

    def __str__(self):
        return self.name

    def clean(self):
        super(Task, self).clean()

        # Check if the instance to clean has an owner.
        # A form can exclude the owner field.. in which case the following checks can be skipped.
        if not hasattr(self, "owner"):
            return

        # Prevent the creation of a task for a project that is not owned.
        if self.owner and self.project and self.owner != self.project.owner:
            raise SuspiciousOperation("Cannot create a Task for a foreign project.")

        # Prevent duplicate names if the project was not set.
        if self.owner and not self.project:
            duplicates = Task.objects.filter(owner=self.owner, name=self.name, project__isnull=True)
            # Prevent a task from finding itself as a duplicate.
            if self.pk:
                duplicates = duplicates.exclude(pk=self.pk)
            # If a task was still found.. the current one is a duplicate.
            if duplicates.exists():
                raise ValidationError("A Task with this name and owner and without a project exists already.")

