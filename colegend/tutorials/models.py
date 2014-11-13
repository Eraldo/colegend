from django.db import models
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Tutorial(AutoUrlMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="What is the idea? How to use the current implementation.")

    def __str__(self):
        return self.name
