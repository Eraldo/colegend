from django.db import models

__author__ = 'eraldo'


class StatusManager(models.Manager):
    def open(self):
        return self.filter(type=Status.OPEN)

    def closed(self):
        return self.filter(type=Status.CLOSED)


class Status(models.Model):
    """
    Django model representing a processing state.
    """
    name = models.CharField(max_length=50, unique=True)

    OPEN = "open"
    CLOSED = "closed"
    DEFAULT = OPEN
    TYPES = (
        (OPEN, "open"),
        (CLOSED, "closed"),
    )
    type = models.CharField(default=DEFAULT, max_length=50, choices=TYPES)
    order = models.PositiveIntegerField(unique=True)
    DEFAULT_PK = 1

    objects = StatusManager()

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['order']

    def __str__(self):
        return self.name

    def open(self):
        return self.type == self.OPEN

    def closed(self):
        return self.type == self.CLOSED

