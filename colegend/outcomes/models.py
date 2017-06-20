from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.intuitive_duration.modelfields import IntuitiveDurationField
from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet, TimeStampedBase
from colegend.scopes.models import ScopeField
from colegend.tags.models import TaggableBase


class OutcomeQuerySet(OwnedQuerySet):
    def scheduled(self, date=None, end=None):
        date = date or timezone.now().date()
        if end:
            queryset = self.filter(date__range=[date, end])
        else:
            queryset = self.filter(date=date)
        return queryset.order_by('date')

    def deadlined(self, date=None, end=None):
        date = date or timezone.now().date()
        if end:
            queryset = self.filter(deadline__range=[date, end])
        else:
            queryset = self.filter(deadline=date)
        return queryset.order_by('deadline')

    def open(self):
        queryset = self.exclude(status__in=[Outcome.DONE, Outcome.CANCELED])
        return queryset

    def closed(self):
        queryset = self.filter(status__in=[Outcome.DONE, Outcome.CANCELED])
        return queryset


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

    OPEN = 1
    WAITING = 2
    DONE = 3
    CANCELED = 4
    STATUSES_OPEN = [OPEN, WAITING]
    STATUSES_CLOSED = [CANCELED, DONE]
    STATUSES = STATUSES_OPEN + STATUSES_CLOSED
    STATUS_CHOICES = (
        (OPEN, _('open')),
        (WAITING, _('waiting')),
        (DONE, _('done')),
        (CANCELED, _('canceled')),
    )
    status = models.PositiveSmallIntegerField(
        _('status'),
        choices=STATUS_CHOICES,
        default=OPEN,
    )
    inbox = models.BooleanField(default=True)
    scope = ScopeField()
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
