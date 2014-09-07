from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from lib.models import TrackedBase, OwnedQueryMixin, AutoUrlMixin

__author__ = 'eraldo'


class VisionQuerySet(OwnedQueryMixin, QuerySet):
    pass


class Vision(AutoUrlMixin, TrackedBase, models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    objects = VisionQuerySet.as_manager()

    def __str__(self):
        return self.name
