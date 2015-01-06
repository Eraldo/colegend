from django.conf import settings
from django.db import models

# Create your models here.
from markitup.fields import MarkupField
from categories.models import Category
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Challenge(AutoUrlMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    content = MarkupField(help_text="What is this challenge about? How can I do this challenge?")

    category = models.ForeignKey(Category)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    source = models.TextField(help_text="Where is the content from? URL? Author?", blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class Module(AutoUrlMixin, models.Model):
#     category = models.ForeignKey(Category)
