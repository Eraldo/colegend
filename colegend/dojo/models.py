from django.conf import settings
from django.db import models
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Module(AutoUrlMixin, models.Model):
    """
    A course module with some content to learn about and practise.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="A compact description of the theory or concept followed by an exercise.")

    category = models.ForeignKey(Category)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    source = models.TextField(help_text="Where is the content from? URL? Author?", blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
