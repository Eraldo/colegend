from django.db import models
from django.utils import timezone

__author__ = 'eraldo'


class FeatureManager(models.Manager):
    pass


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)
    date_published = models.DateField(default=timezone.now())

    objects = FeatureManager()

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.name
