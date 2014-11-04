from django.conf import settings
from django.db import models
from django.utils import timezone
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Gathering(AutoUrlMixin, models.Model):
    date = models.DateTimeField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return timezone.localtime(self.date).strftime('%A %Y-%m-%d %H:%M')
