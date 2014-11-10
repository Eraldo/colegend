from django.conf import settings
from django.db import models
from django.utils import timezone
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class Gathering(AutoUrlMixin, models.Model):
    date = models.DateTimeField()
    LOCATION_DEFAULT = "http://gathering.colegend.org/"
    location = models.CharField(max_length=200, default=LOCATION_DEFAULT)
    online = models.BooleanField(default=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return timezone.localtime(self.date).strftime('%A %Y-%m-%d %H:%M')
