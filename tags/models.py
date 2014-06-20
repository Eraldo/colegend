from django.db import models
from taggit.managers import TaggableManager

__author__ = 'eraldo'


class TaggableBase(models.Model):
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True