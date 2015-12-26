from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from core.models import SingleOwnedBase, TimeStampedBase


class OuterCall(SingleOwnedBase, TimeStampedBase):
    """
    A django model representing the legend's trigger to join coLegend.
    """
    trigger = models.TextField(
        verbose_name=_("How did you find out about coLegend?")
    )
    referrer = models.CharField(
        verbose_name=_("Who was your contact person?"),
        max_length=255, blank=True,
        help_text=_('If someone told you about coLegend: Who was it?'))

    def __str__(self):
        return "{}'s outer call".format(self.owner)

    def get_absolute_url(self):
        return reverse('outer-call:update')
