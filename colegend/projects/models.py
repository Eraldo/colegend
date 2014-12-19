from django.db import models
from django.db.models import Min
from django.db.models.query import QuerySet
from markitup.fields import MarkupField
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin, ValidateModelMixin
from statuses.models import Status
from statuses.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class Project(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = MarkupField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    deadline = models.DateField(blank=True, null=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ["status", "name"]
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name

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
