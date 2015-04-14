from django.core.exceptions import ValidationError, SuspiciousOperation
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin, ValidateModelMixin, StatusTrackedBase
from projects.models import Project
from statuses.models import Status
from statuses.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class TaskQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class Task(ValidateModelMixin, AutoUrlMixin, OwnedBase, StatusTrackedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a task.
    """
    # > owner: User
    project = models.ForeignKey(Project, blank=True, null=True, related_name="tasks")
    name = models.CharField(max_length=100, help_text="Tip: Use a verb as the first word.")

    description = MarkupField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    date = models.DateField(blank=True, null=True, help_text="When will I start/continue?")
    deadline = models.DateField(blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    objects = TaskQuerySet.as_manager()

    class Meta:
        ordering = ["status", "project", "-modification_date"]
        unique_together = ('owner', 'project', 'name')

    def __str__(self):
        return self.name

    @property
    def open(self):
        return self.status in Status.objects.open()

    @property
    def closed(self):
        return self.status in Status.objects.closed()

    def complete(self):
        self.status = Status.objects.get(name="done")
        self.save()
        return True  # worked

    def get_due_string(self):
        date = self.date
        deadline = self.deadline
        if not date or deadline:
            return
        today = timezone.now().date()
        if date and date < today or deadline and deadline < today:
            return "overdue"
        elif date and date == today or deadline and deadline == today:
            return "due"
        else:
            return ""

    @property
    def is_overdue(self):
        date = self.date
        deadline = self.deadline
        if not date or deadline:
            return False
        today = timezone.now().date()
        if date and date < today:
            return True
        elif deadline and deadline < today:
            return True
        else:
            return False

    def clean(self):
        super(Task, self).clean()

        # Check if the instance to clean has an owner.
        # A form can exclude the owner field.. in which case the following checks can be skipped.
        if not hasattr(self, "owner"):
            return

        # Prevent the creation of a task for a project that is not owned.
        if self.owner and self.project and self.owner != self.project.owner:
            raise SuspiciousOperation("Cannot create a Task for a foreign project.")
