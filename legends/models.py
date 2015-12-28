from django.core.urlresolvers import reverse
from django.db import models

from core.models import AutoOwnedBase, TimeStampedBase


class Legend(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the user as a whole complete with:
    + general profile information
    + hero profile
    + demon profile
    """
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return "Legend {}".format(self.owner)

    def get_absolute_url(self):
        return reverse('legends:detail', kwargs={'owner': self.owner.username})
