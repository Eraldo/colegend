from django.db import models
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Card(AutoUrlMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="cards")

    def __str__(self):
        return self.name
