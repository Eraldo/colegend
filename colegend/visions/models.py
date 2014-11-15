from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from markitup.fields import MarkupField
from lib.models import TrackedBase, OwnedQueryMixin, AutoUrlMixin, ValidateModelMixin

__author__ = 'eraldo'


class VisionQuerySet(OwnedQueryMixin, QuerySet):
    pass


class Vision(ValidateModelMixin, AutoUrlMixin, TrackedBase, models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)

    content = MarkupField(blank=True)

    objects = VisionQuerySet.as_manager()

    class Meta:
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name
