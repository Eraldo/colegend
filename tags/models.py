from django.db import models
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItem
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Tag(AutoUrlMixin, Tag):
    """
    A django model representing a text-tag.
    Note:
    This is a proxy class: all it's functionality is inherited by the Tag model of django-taggit.
    """
    class Meta:
        proxy = True


class TaggedItem(TaggedItem):
    """
    A django model representing an item that is tagged.
    Note:
    This is a proxy class: all it's functionality is inherited by the Tag model of django-taggit.
    """
    class Meta:
        proxy = True



class TaggableBase(models.Model):
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True