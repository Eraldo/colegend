from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoUrlsMixin, TimeStampedBase
from colegend.journals.models import Journal
from .utils import get_current_year, get_current_week
from colegend.tags.models import TaggableBase


class WeekEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)


class WeekEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's daily journal entry.
    """
    journal = models.ForeignKey(Journal, related_name="weekentries")
    year = models.PositiveIntegerField(default=get_current_year, validators=[MaxValueValidator(4000)])
    week = models.PositiveIntegerField(default=get_current_week, validators=[MaxValueValidator(54)])
    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("What were the most important experiences/topics this week?")
    )
    content = MarkdownField()

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

    @property
    def detail_url(self):
        return reverse('weekentries:detail', kwargs={'pk': self.pk})