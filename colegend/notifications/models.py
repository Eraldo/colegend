from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from lib.models import TimeStampedBase, OwnedQueryMixin, AutoUrlMixin

__author__ = 'eraldo'


class NotificationQuerySet(OwnedQueryMixin, QuerySet):
    def unread(self):
        return self.filter(read=False)

    def read(self):
        return self.filter(read=True)

    def top(self):
        return self[:7]


class Notification(AutoUrlMixin, TimeStampedBase):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notifications")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    read = models.BooleanField(default=False)

    objects = NotificationQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-creation_date"]
