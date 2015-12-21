from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from core.models import AutoOwnedBase, TimeStampedBase


class GuideRelation(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the relation between a user and his guide.
    """
    # TODO: make sure that guide and guidee are never the same user.

    guide = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='guidee_relations',
        null=True)
    outer_call_checked = models.BooleanField(
        verbose_name=_("Talked about Outer Call"),
        default=False)
    inner_call_checked = models.BooleanField(
        verbose_name=_("Talked about Inner Call"),
        default=False)
    coLegend_checked = models.BooleanField(
        verbose_name=_("Answered any questions about coLegend"),
        default=False)
    guiding_checked = models.BooleanField(
        verbose_name=_("Talked about becoming a Guide"),
        default=False)

    def __str__(self):
        return "Guide relation: {} - {}".format(self.owner, self.guide)

    def get_absolute_url(self):
        return reverse('guides:detail', kwargs={'owner': self.owner.username})
