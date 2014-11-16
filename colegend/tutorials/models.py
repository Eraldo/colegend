from annoying.functions import get_object_or_None
from django.db import models
from markitup.fields import MarkupField
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Tutorial(AutoUrlMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = MarkupField(help_text="What is the idea? How to use the current implementation.")

    def __str__(self):
        return self.name


def get_tutorial(name):
    return get_object_or_None(Tutorial, name=name)
