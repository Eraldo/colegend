from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from core.models import SingleOwnedBase, TimeStampedBase


class InnerCall(SingleOwnedBase, TimeStampedBase):
    """
    A django model representing the legend's motivation to join coLegend.
    """
    motivation = models.TextField(_("What was your motivation to join coLegend?"))
    change = models.TextField(_("What do you want to change in your life?"))
    drive = models.PositiveIntegerField(
        verbose_name=_("How strong is your drive to get there?"),
        help_text=_("10 = very strong, 1 = not strong at all"))
    wishes = models.TextField(
        verbose_name=_("What are your wishes for this platform?"),
        blank=True)
    other = models.TextField(
        verbose_name=_("Is there anything else you want to share? :)"),
        blank=True)

    def __str__(self):
        return "{}'s inner call".format(self.owner)

    def get_absolute_url(self):
        return reverse('inner-call:update')
