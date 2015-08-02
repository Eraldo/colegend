from django.db import models
from django.db.models.query import QuerySet
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase, OwnedQueryMixin, ValidateModelMixin

__author__ = 'eraldo'


class TagQuerySet(OwnedQueryMixin, QuerySet):
    pass


class Tag(ValidateModelMixin, AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a text-tag.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = MarkupField(blank=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    objects = TagQuerySet.as_manager()

    class Meta:
        ordering = ["name"]
        unique_together = ('owner', 'name')
        default_related_name = "tags"

    def __str__(self):
        return self.name


class TaggableBase(models.Model):
    tags = models.ManyToManyField(Tag, blank=True, related_name="%(app_label)s")

    class Meta:
        abstract = True
