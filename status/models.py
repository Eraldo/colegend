from django.db import models

__author__ = 'eraldo'


class StatusManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

    def open(self):
        return self.filter(type=Status.OPEN)

    def closed(self):
        return self.filter(type=Status.CLOSED)

    def default(self):
        return Status.DEFAULT


class Status(models.Model):
    """
    Django model representing a processing state.
    """
    objects = StatusManager()

    name = models.CharField(max_length=20, unique=True)
    OPEN = "open"
    CLOSED = "closed"
    DEFAULT = OPEN
    TYPES = (
        (OPEN, "open"),
        (CLOSED, "closed"),
    )
    type = models.CharField(default=DEFAULT, max_length=25, choices=TYPES)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Status"
        ordering = ['order']

    def __str__(self):
        return self.name

    def natural_key(self):
        return [self.name]

    def open(self):
        return self.type == self.OPEN

    def closed(self):
        return self.type == self.CLOSED

