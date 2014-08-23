from django.db import models

__author__ = 'eraldo'


class Meeting(models.Model):
    date = models.DateTimeField(blank=True, null=True)
