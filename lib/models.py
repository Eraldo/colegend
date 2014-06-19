from django.db import models

__author__ = 'eraldo'


class TimeStampedModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LoggableModel(models.Model):
    history = models.TextField(blank=True)

    class Meta:
        abstract = True