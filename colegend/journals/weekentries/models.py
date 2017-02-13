from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoUrlsMixin, TimeStampedBase
from colegend.journals.models import Journal, JournalPage
from colegend.journals.scopes import Week
from colegend.outcomes.models import Outcome
from .utils import get_current_year, get_current_week
from colegend.tags.models import TaggableBase


class WeekEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)

    def current(self):
        today = timezone.now().date()
        scope = Week(date=today)
        return self.filter(year=scope.year.number, week=scope.number)


class WeekEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's daily journal entry.
    """
    journal = models.ForeignKey(Journal, related_name="weekentries")
    year = models.PositiveIntegerField(default=get_current_year, validators=[MaxValueValidator(4000)])
    week = models.PositiveIntegerField(default=get_current_week, validators=[MaxValueValidator(54)])
    focus = models.TextField(blank=True)
    outcome_1 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='week_focus_1',
    )
    outcome_2 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='week_focus_2',
    )
    outcome_3 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='week_focus_3',
    )
    outcome_4 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='week_focus_4',
    )

    @property
    def outcomes(self):
        outcomes = [self.outcome_1, self.outcome_2, self.outcome_3, self.outcome_4]
        return [outcome for outcome in outcomes if outcome]

    content = MarkdownField()
    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("What were the most important experiences/topics this week?")
    )

    objects = WeekEntryQuerySet.as_manager()

    class Meta:
        verbose_name = _('Week Entry')
        verbose_name_plural = _('Weekentries')
        unique_together = ['journal', 'year', 'week']
        ordering = ['-year', '-week']

    def __str__(self):
        return '{}-W{}'.format(self.year, self.week)

    def owned_by(self, user):
        if self.journal.owned_by(user):
            return True
        else:
            return False

    @property
    def date(self):
        return timezone.datetime.strptime('{}-W{}-1'.format(self.year, self.week), "%Y-W%W-%w").date()

    @property
    def dates(self):
        return '{} - {}'.format(self.start, self.end)

    @property
    def start(self):
        return self.date

    @property
    def end(self):
        return self.start + timezone.timedelta(days=6)

    @property
    def number(self):
        return self.date.isocalendar()[1]

    def get_absolute_url(self):
        page = JournalPage.objects.first()
        return page.url + page.reverse_subpage('week', kwargs={'date': Week(self.date)})

