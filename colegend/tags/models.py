from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import string_concat
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

    description = models.TextField(blank=True)

    objects = TagQuerySet.as_manager()

    class Meta:
        ordering = ["name"]
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name


class TaggableBase(models.Model):
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="%(app_label)s")
    # using string_concat because format is not lazy.
    tags.help_text = string_concat(
        "<a href='",
        reverse_lazy("tags:tag_new"),
        "' target='_blank'><i class='fa fa-plus-circle' style='color: green;'></i> New Tag</a>",
        "- <small>*Refresh page to view new tag.</small><br>"
    )

    class Meta:
        abstract = True
