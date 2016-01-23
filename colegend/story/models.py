from django.db import models

from colegend.core.models import TimeStampedBase, SingleOwnedBase

__author__ = 'Eraldo Energy'


class WelcomeTreeLeaf(SingleOwnedBase, TimeStampedBase):
    content = models.TextField()

    def __str__(self):
        return "{}'s welcome leaf".format(self.owner)

    class Meta:
        verbose_name_plural = "Welcome tree leaves"
