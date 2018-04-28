from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from ordered_model.models import OrderedModel

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
        queryset = self.exclude(status__in=Outcome.STATUSES_CLOSED)
        return queryset

    def closed(self):
        queryset = self.filter(status__in=Outcome.STATUSES_CLOSED)
        return queryset

    def search(self, query):
        queryset = self.filter(Q(name__icontains=query) | Q(description__icontains=query))
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

    CURRENT = 'current'
    WAITING = 'waiting'
    FUTURE = 'future'
    DONE = 'done'
    CANCELED = 'canceled'

    STATUSES_OPEN = [CURRENT, WAITING, FUTURE]
    STATUSES_CLOSED = [DONE, CANCELED]
    STATUSES = STATUSES_OPEN + STATUSES_CLOSED
    STATUS_CHOICES = (
        (CURRENT, _('open')),
        (WAITING, _('waiting')),
        (FUTURE, _('canceled')),
        (DONE, _('done')),
        (CANCELED, _('canceled')),
    )
    status = models.CharField(
        _('status'),
        choices=STATUS_CHOICES,
        default=CURRENT,
        max_length=10,
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
        blank=True, null=True,
    )

    estimate = IntuitiveDurationField(
        _('time estimate'),
        blank=True,
        null=True
    )
    completed_at = models.DateTimeField(
        _('completed at'),
        null=True, blank=True,
    )
    score = models.PositiveSmallIntegerField(
        verbose_name=_('score'),
        default=1000,
    )
    comparisons = models.PositiveSmallIntegerField(
        verbose_name=_('sore comparisons'),
        default=0,
    )

    @property
    def is_provisional(self):
        return self.comparisons < 10

    objects = OutcomeQuerySet.as_manager()

    class Meta:
        verbose_name = _('outcome')
        verbose_name_plural = _('outcomes')
        default_related_name = 'outcomes'
        ordering = ['-score']

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return self.status in self.STATUSES_OPEN

    @property
    def is_inactive(self):
        return self.status in self.STATUSES_CLOSED

    @property
    def is_focus(self):
        """Checking if the outcome is currently set as focus in a scope."""

        today = timezone.localtime(timezone.now()).date()
        if self.focus_1.filter(end__gte=today).exists() or \
            self.focus_2.filter(end__gte=today).exists() or \
            self.focus_3.filter(end__gte=today).exists() or \
            self.focus_4.filter(end__gte=today).exists():
            return True
        return False

    @property
    def next_step(self):
        return self.steps.filter(completed_at__isnull=True).first()


class Step(TimeStampedBase, OrderedModel):
    outcome = models.ForeignKey(
        to=Outcome,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    completed_at = models.DateTimeField(
        _('completed at'),
        null=True, blank=True,
    )
    order_with_respect_to = 'outcome'

    def toggle(self):
        if self.completed_at:
            self.mark_incomplete()
        else:
            self.mark_complete()

    def mark_complete(self):
        if not self.completed_at:
            timestamp = timezone.now()
            self.completed_at = timestamp
            self.save(update_fields=['completed_at'])

    def mark_incomplete(self):
        self.completed_at = None
        self.save(update_fields=['completed_at'])

    @property
    def is_open(self):
        return not self.is_open

    @property
    def is_closed(self):
        return bool(self.completed_at)

    class Meta(OrderedModel.Meta):
        default_related_name = 'steps'
        unique_together = ['outcome', 'name']

    def __str__(self):
        return self.name
