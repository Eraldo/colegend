# from django.core.validators import MaxValueValidator
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
#
# from colegend.core.fields import MarkdownField
# from colegend.core.models import AutoUrlsMixin, TimeStampedBase
# from colegend.journals.models import Journal, JournalPage
# from colegend.journals.scopes import Year
# from .utils import get_current_year
# from colegend.tags.models import TaggableBase
#
#
# class YearEntryQuerySet(models.QuerySet):
#     def owned_by(self, user):
#         return self.filter(journal__owner=user)
#
#     def current(self):
#         today = timezone.now().date()
#         scope = Year(date=today)
#         return self.filter(year=scope.number)
#
#
# class YearEntry(AutoUrlsMixin, TaggableBase, TimeStampedBase):
#     """
#     A django model representing a user's daily journal entry.
#     """
#     journal = models.ForeignKey(Journal, related_name="yearentries")
#     year = models.PositiveIntegerField(default=get_current_year, validators=[MaxValueValidator(4000)])
#
#     content = MarkdownField()
#     keywords = models.CharField(
#         max_length=255,
#         blank=True,
#         help_text=_("What were the most important experiences/topics this year?")
#     )
#
#     objects = YearEntryQuerySet.as_manager()
#
#     class Meta:
#         verbose_name = _('Year Entry')
#         verbose_name_plural = _('Yearentries')
#         unique_together = ['journal', 'year']
#         ordering = ['-year']
#
#     def __str__(self):
#         return '{}'.format(self.year)
#
#     def owned_by(self, user):
#         if self.journal.owned_by(user):
#             return True
#         else:
#             return False
#
#     @property
#     def scope(self):
#         return Year('{}'.format(self.year))
#
#     @property
#     def date(self):
#         return self.scope.date
#
#     @property
#     def dates(self):
#         return '{} - {}'.format(self.scope.start, self.scope.end)
#
#     @property
#     def start(self):
#         return self.scope.start
#
#     @property
#     def end(self):
#         return self.scope.end
#
#     @property
#     def number(self):
#         return self.scope.number
#
#     def get_absolute_url(self):
#         page = JournalPage.objects.first()
#         return page.url + page.reverse_subpage('year', kwargs={'date': Year(self.date)})
