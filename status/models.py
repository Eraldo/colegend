from django.db import models

__author__ = 'eraldo'


class StatusManager(models.Manager):
    def open(self):
        return self.filter(type=Status.OPEN)

    def closed(self):
        return self.filter(type=Status.CLOSED)

    def default(self):
        return Status.DEFAULT


class Status(models.Model):
    name = models.CharField(max_length=20, unique=True)
    OPEN = 1
    CLOSED = 2
    DEFAULT = OPEN
    TYPES = (
        (OPEN, "open"),
        (CLOSED, "closed"),
    )
    type = models.IntegerField(default=DEFAULT, max_length=1, choices=TYPES)
    order = models.PositiveIntegerField()
    objects = StatusManager()

    def __str__(self):
        return self.name

    def open(self):
        return self.type == self.OPEN

    def closed(self):
        return self.type == self.CLOSED

    class Meta:
        verbose_name_plural = "Status"
        ordering = ['order']