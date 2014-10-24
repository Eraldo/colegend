from django.conf import settings
from django.db import models

# Create your models here.
from dojo.models import Category
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Challenge(AutoUrlMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="A short description of the course content.")

    category = models.ForeignKey(Category)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    source = models.TextField(help_text="Where is the content from? URL? Author?", blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
