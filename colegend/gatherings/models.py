from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models
from django.utils import timezone
from markitup.fields import MarkupField
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


class GatheringQuerySet(models.QuerySet):
    def current(self):
        """
        Get the currently happening gathering.
        :return: A Gathering object or None.
        """
        now = timezone.now()
        try:
            current = self.filter(start__lte=now, end__gte=now).first()
        except Gathering.DoesNotExist:
            current = None
        return current

    def next(self):
        """
        Get the next upcoming gathering.
        :return: A Gathering object or None.
        """
        now = timezone.now()
        try:
            # if there is one right now.. return it..
            current = self.current()
            if current:
                return current
            # return the next one (oldest of future ones)
            return self.filter(start__gte=now).last()
        except Gathering.DoesNotExist:
            return None


class Gathering(AutoUrlMixin, models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    LOCATION_DEFAULT = "http://gathering.colegend.org/"
    location = models.CharField(max_length=200, default=LOCATION_DEFAULT)
    online = models.BooleanField(default=True)
    topic = models.CharField(max_length=100, blank=True)
    notes = MarkupField(blank=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="gatherings_participated")
    host = models.ForeignKey(settings.AUTH_USER_MODEL)

    objects = GatheringQuerySet.as_manager()

    class Meta:
        ordering = ["-start"]

    def __str__(self):
        return timezone.localtime(self.start).strftime('%A %Y-%m-%d %H:%M')

    def get_location_display(self):
        if self.online:
            return "virtual room"
        else:
            return self.location
