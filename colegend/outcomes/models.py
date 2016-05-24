from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet


class OutcomeQuerySet(OwnedQuerySet):
    pass


class Outcome(AutoUrlsMixin, OwnedBase):
    """
    A django model representing a user's outcome.
    """
    name = models.CharField(
        _('name'),
        max_length=255,
    )

    objects = OutcomeQuerySet.as_manager()

    class Meta:
        verbose_name = _('outcome')
        verbose_name_plural = _('outcomes')
        default_related_name = 'outcomes'

    def __str__(self):
        return self.name
