from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManagerMixin
from lib.models import TrackedBase, AutoUrlMixin, OwnedBase, OwnedQueryMixin
from status.models import Status
from status.utils import StatusQueryMixin
from tags.models import TaggableBase

__author__ = 'eraldo'


class ProjectQuerySet(StatusQueryMixin, OwnedQueryMixin, QuerySet):
    pass


class ProjectManager(PassThroughManagerMixin, models.Manager):
    pass


class Project(AutoUrlMixin, OwnedBase, TrackedBase, TaggableBase, models.Model):
    """
    A django model representing a project.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, default=Status.DEFAULT_PK)
    deadline = models.DateField(blank=True, null=True)

    objects = ProjectManager.for_queryset_class(ProjectQuerySet)()

    class Meta:
        unique_together = (('owner', 'name'),)

    def __str__(self):
        return self.name

