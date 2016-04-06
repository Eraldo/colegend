from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase, AutoUrlsMixin, TimeStampedBase, OwnedQuerySet


class DonationQuerySet(OwnedQuerySet):
    def total(self):
        """
        Return the sum of all donations.
        """
        total = self.aggregate(Sum('amount')).get('amount__sum')
        return total


class Donation(AutoUrlsMixin, TimeStampedBase, OwnedBase):
    """
    A django model representing a user's donation.
    """
    date = models.DateField(
        verbose_name=_('date'),
    )
    amount = models.DecimalField(
        verbose_name=_('amount'),
        max_digits=6, decimal_places=2,
        help_text=_('€')
    )
    notes = models.TextField(
        verbose_name=_('notes'),
        blank=True,
    )

    objects = DonationQuerySet.as_manager()

    class Meta:
        verbose_name = _('donation')
        verbose_name_plural = _('donations')
        default_related_name = 'donations'

    def __str__(self):
        return '{}: €{} {}'.format(self.date, self.amount, self.owner)
