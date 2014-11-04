from django.db import models
from django.utils import timezone

__author__ = 'eraldo'


class Gathering(models.Model):
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return timezone.localtime(self.date).strftime('%A %Y-%m-%d %H:%M')
