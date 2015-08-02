from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.query import QuerySet
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin, ValidateModelMixin, StatusTrackedBase
from statuses.models import Status
from statuses.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class Project(ValidateModelMixin, AutoUrlMixin, OwnedBase, StatusTrackedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = MarkupField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    date = models.DateField(blank=True, null=True, help_text="When will I start/continue?")
    deadline = models.DateField(blank=True, null=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ["status", "-modification_date"]
        unique_together = ('owner', 'name')
        default_related_name = "projects"

    def __str__(self):
        return self.name

    @property
    def is_open(self):
        return self.status in Status.objects.open()

    @property
    def is_closed(self):
        return self.status in Status.objects.closed()

    def complete(self):
        self.status = Status.objects.get(name="done")
        self.save()
        return True  # worked

    @property
    def next_step(self):
        tasks = self.tasks
        if tasks.exists():
            return tasks.filter(status__name="next").first()

    @property
    def has_next_step(self):
        if self.next_step:
            return True
        else:
            return False
