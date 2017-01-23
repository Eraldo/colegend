from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoUrlsMixin, TimeStampedBase
from colegend.journals.models import Journal, JournalPage
from colegend.journals.scopes import Quarter
from .utils import get_current_year, get_current_quarter
from colegend.tags.models import TaggableBase


class QuarterEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)

    def current(self):
        today = timezone.now().date()
        scope = Quarter(date=today)
        return self.filter(year=scope.year, quarter=scope.number)


class QuarterEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's daily journal entry.
    """
    journal = models.ForeignKey(Journal, related_name="quarterentries")
    year = models.PositiveIntegerField(default=get_current_year, validators=[MaxValueValidator(4000)])
    quarter = models.PositiveIntegerField(default=get_current_quarter, validators=[MaxValueValidator(4)])
    focus = models.TextField(blank=True)
    content = MarkdownField()
    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("What were the most important experiences/topics this quarter?")
    )

    objects = QuarterEntryQuerySet.as_manager()

    class Meta:
        verbose_name = _('Quarter Entry')
        verbose_name_plural = _('Quarterentries')
        unique_together = ['journal', 'year', 'quarter']
        ordering = ['-year', '-quarter']

    def __str__(self):
        return '{}-Q{}'.format(self.year, self.quarter)

    def owned_by(self, user):
        if self.journal.owned_by(user):
            return True
        else:
            return False

    @property
    def scope(self):
        return Quarter('{}-Q{}'.format(self.year, self.quarter))

    @property
    def date(self):
        return self.scope.date

    @property
    def dates(self):
        return '{} - {}'.format(self.scope.start, self.scope.end)

    @property
    def start(self):
        return self.scope.start

    @property
    def end(self):
        return self.scope.end

    @property
    def number(self):
        return self.scope.number

    def get_absolute_url(self):
        page = JournalPage.objects.first()
        return page.url + page.reverse_subpage('quarter', kwargs={'date': Quarter(self.date)})
