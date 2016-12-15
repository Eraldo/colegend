from calendar import monthrange, month_name

from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoUrlsMixin, TimeStampedBase
from colegend.journals.models import Journal, JournalPage
from colegend.journals.scopes import Month
from .utils import get_current_year, get_current_month
from colegend.tags.models import TaggableBase


class MonthEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)


class MonthEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's daily journal entry.
    """
    journal = models.ForeignKey(Journal, related_name="monthentries")
    year = models.PositiveIntegerField(default=get_current_year, validators=[MaxValueValidator(4000)])
    month = models.PositiveIntegerField(default=get_current_month, validators=[MaxValueValidator(12)])
    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("What were the most important experiences/topics this month?")
    )
    content = MarkdownField()

    objects = MonthEntryQuerySet.as_manager()

    class Meta:
        verbose_name = _('Month Entry')
        verbose_name_plural = _('Monthentries')
        unique_together = ['journal', 'year', 'month']
        ordering = ['-year', '-month']

    def __str__(self):
        return '{}-M{}'.format(self.year, self.month)

    def owned_by(self, user):
        if self.journal.owned_by(user):
            return True
        else:
            return False

    @property
    def date(self):
        return timezone.datetime.strptime('{}-M{}'.format(self.year, self.month), "%Y-M%m").date()

    @property
    def dates(self):
        return '{} - {}'.format(self.start, self.end)

    @property
    def start(self):
        return self.date

    @property
    def end(self):
        days_in_month = monthrange(self.year, self.month)[1]
        return self.start + timezone.timedelta(days=days_in_month-1)

    @property
    def number(self):
        return self.month

    def get_absolute_url(self):
        page = JournalPage.objects.first()
        return page.url + page.reverse_subpage('month', kwargs={'date': Month(self.date)})
