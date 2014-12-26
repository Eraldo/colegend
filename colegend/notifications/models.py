from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from lib.models import TimeStampedBase, OwnedQueryMixin, AutoUrlMixin
from users.models import User

__author__ = 'eraldo'


class NotificationQuerySet(OwnedQueryMixin, QuerySet):
    def unread(self):
        return self.filter(read=False)

    def read(self):
        return self.filter(read=True)

    def top(self):
        return self[:7]

    def broadcast(self, name, description=""):
        """
        Creates a notification for every accepted user.
        TODO: Implement.. Will replace any instance of '{user}' with the actual username.
        :param name:
        :param description:
        :return:
        """
        self.bulk_create(
            [Notification(
                owner=owner,
                name=name.replace("{user}", owner.username),
                description=description.replace("{user}", owner.username)
            ) for owner in User.objects.accepted()]
        )

    def mark_as_read(self):
        self.update(read=True)


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
