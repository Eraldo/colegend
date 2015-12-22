from django.db import models

from core.models import TimeStampedBase, SingleOwnedBase

__author__ = 'Eraldo Energy'


class WelcomeTreeLeaf(SingleOwnedBase, TimeStampedBase):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Welcome tree leaves"
