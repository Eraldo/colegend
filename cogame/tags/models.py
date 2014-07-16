from django.db import models
from lib.models import AutoUrlMixin, OwnedBase, TrackedBase

__author__ = 'eraldo'


class TagManager(models.Manager):
    def get_by_natural_key(self, owner, name):
        return self.get(owner=owner, name=name)


class Tag(AutoUrlMixin, OwnedBase, TrackedBase, models.Model):
    """
    A django model representing a text-tag.
    """
    # > owner: User
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    objects = TagManager()

    class Meta:
        ordering = ["name"]
        unique_together = (('owner', 'name'),)

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.owner, self.name]

    natural_key.dependencies = ['users.user']


class TaggableBase(models.Model):
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="%(app_label)s")

    class Meta:
        abstract = True
