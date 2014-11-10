from django.conf import settings
from django.db import models
from lib.models import AutoUrlMixin
from categories.models import Category

__author__ = 'eraldo'


class Module(AutoUrlMixin, models.Model):
    """
    A course module with some content to learn about and practise.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="A short description of the course content.")

    content = models.TextField(help_text="A compact explanation of the theory or concept followed by an exercise.")

    category = models.ForeignKey(Category)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    source = models.TextField(help_text="Where is the content from? URL? Author?", blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
