from django.db import models
from core.models import TimeStampedBase, AutoOwnedBase


class Legend(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the coLegend story aka 'legend'.
    """
    prologue = models.BooleanField(default=False)

    def __str__(self):
        return "Legend path of {}".format(self.owner)
