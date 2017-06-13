from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField, DateField
from colegend.core.models import AutoUrlsMixin, TimeStampedBase
from colegend.core.validators import validate_date_today_tomorrow_or_past
from colegend.journals.models import Journal, JournalPage
from colegend.tags.models import TaggableBase


class DayEntryQuerySet(models.QuerySet):
    def owned_by(self, user):
        return self.filter(journal__owner=user)

    def current(self):
        today = timezone.now().date()
        return self.filter(date=today)


class DayEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
    """
    A django model representing a user's daily journal entry.
    """
    journal = models.ForeignKey(Journal, related_name="dayentries")
    date = DateField(default=timezone.datetime.today, validators=[validate_date_today_tomorrow_or_past])
    locations = models.CharField(max_length=255, help_text="Separated by ';'")

    keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="What were the most important experiences/topics on this day?")
    content = MarkdownField()

    objects = DayEntryQuerySet.as_manager()

    class Meta:
        verbose_name = _('Day Entry')
        verbose_name_plural = _('Dayentries')
        unique_together = ['journal', 'date']
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return str(self.date)

    def owned_by(self, user):
        if self.journal.owned_by(user):
            return True
        else:
            return False

    @property
    def detail_url(self):
        page = JournalPage.objects.first()
        return page.url + page.reverse_subpage('day', kwargs={'date': self.date})
