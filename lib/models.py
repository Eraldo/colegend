from django.db import models
from taggit.managers import TaggableManager

__author__ = 'eraldo'


class TimeStampedBase(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LoggableBase(models.Model):
    history = models.TextField(blank=True)

    class Meta:
        abstract = True


class TrackedBase(TimeStampedBase, LoggableBase):

    class Meta:
        abstract = True


class TaggableBase(models.Model):
    tags = TaggableManager()

    class Meta:
        abstract = True