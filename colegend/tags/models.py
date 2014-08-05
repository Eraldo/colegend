from django.db import models
from django.db.models.query import QuerySet
from model_utils.managers import PassThroughManager
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase, OwnedQueryMixin

__author__ = 'eraldo'


class TagQuerySet(OwnedQueryMixin, QuerySet):
    pass


class TagManager(PassThroughManager, models.Manager):
    pass


class Tag(AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a text-tag.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    objects = TagManager.for_queryset_class(TagQuerySet)()

    class Meta:
        ordering = ["name"]
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name


class TaggableBase(models.Model):
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="%(app_label)s")

    class Meta:
        abstract = True
