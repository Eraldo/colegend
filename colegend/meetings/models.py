from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

__author__ = 'eraldo'


class Meeting(models.Model):
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return timezone.localtime(self.date).strftime('%A %Y-%m-%d %H:%M')
