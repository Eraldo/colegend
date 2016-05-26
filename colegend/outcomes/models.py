from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet, TimeStampedBase
from colegend.tags.models import TaggableBase


class OutcomeQuerySet(OwnedQuerySet):
    pass


class Outcome(AutoUrlsMixin, OwnedBase, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's outcome.
    """
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    description = models.TextField(
        _('description'),
        blank=True,
    )

    OPEN = 0
    WAITING = 1
    CLOSED = 2
    STATUS_CHOICES = (
        (OPEN, _('open')),
        (WAITING, _('waiting')),
        (CLOSED, _('closed')),
    )
    status = models.PositiveSmallIntegerField(
        _('status'),
        choices=STATUS_CHOICES,
        default=OPEN,
    )
    DAILY = 0
    WEEKLY = 1
    MONTHLY = 2
    QUARTERLY = 3
    YEARLY = 4
    SOMETIME = 5
    REVIEW_CHOICES = (
        (DAILY, _('daily')),
        (WEEKLY, _('weekly')),
        (MONTHLY, _('monthly')),
        (QUARTERLY, _('quarterly')),
        (YEARLY, _('yearly')),
        (SOMETIME, _('sometime')),
    )
    review = models.PositiveSmallIntegerField(
        _('review'),
        choices=REVIEW_CHOICES,
        blank=True,
        null=True,
        help_text=_('Minimum review frequency')
    )
    inbox = models.BooleanField(default=False)

    date = models.DateField(
        _('date'),
        blank=True,
        null=True,
        help_text=_('When will I start/continue?'),
    )
    deadline = models.DateField(
        _('deadline'),
        blank=True,
        null=True,
    )

    estimate = IntuitiveDurationField(
        _('time estimate'),
        blank=True,
        null=True
    )

    objects = OutcomeQuerySet.as_manager()

    class Meta:
        verbose_name = _('outcome')
        verbose_name_plural = _('outcomes')
        default_related_name = 'outcomes'
        ordering = ['-modified']

    def __str__(self):
        return self.name
