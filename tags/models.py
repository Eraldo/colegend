from django.db import models
from lib.models import AutoUrlMixin, TimeStampedBase

__author__ = 'eraldo'


class TagManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Tag(AutoUrlMixin, TimeStampedBase, models.Model):
    """
    A django model representing a text-tag.
    """
    name = models.CharField(unique=True, max_length=100)

    objects = TagManager()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]


class TaggableBase(models.Model):
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="%(app_label)s")

    class Meta:
        abstract = True