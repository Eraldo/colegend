from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoOwnedBase, AutoUrlsMixin, OwnedQuerySet
from colegend.journals import scopes


class JournalQuerySet(OwnedQuerySet):
    pass


class Journal(AutoUrlsMixin, AutoOwnedBase):
    """
    A django model representing a user's journal.
    """

    spellchecker = models.BooleanField(default=False)
    day_template = MarkdownField(default=render_to_string('dayentries/template.md'))
    week_template = MarkdownField(default=render_to_string('weekentries/template.md'))
    month_template = MarkdownField(default=render_to_string('monthentries/template.md'))

    objects = JournalQuerySet.as_manager()

    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')

    def __str__(self):
        return "{}'s journal".format(self.owner)

    def reset(self):
        self.spellchecker = False
        self.day_template = render_to_string('dayentries/template.md')
        self.week_template = render_to_string('weekentries/template.md')
        self.month_template = render_to_string('monthentries/template.md')
        self.save()
        return True


class JournalPage(RoutablePageMixin, Page):
    template = 'journals/index.html'

    @staticmethod
    def get_default_date():
        return timezone.now().date()

    def get_context(self, request, *args, scope='day', date=None, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        date = date or self.get_default_date()
        context['scopes'] = scopes.all
        from colegend.journals.forms import DatePickerForm
        context['datepickerform'] = DatePickerForm(initial={'date': date})
        return context

    @route(r'^$')
    @route(r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$')
    def day(self, request, date=None):
        date = date or self.get_default_date()

        context = self.get_context(request)
        context['scope'] = scopes.Day

        return TemplateResponse(
            request,
            self.get_template(request),
            context
        )

    @route(r'^week/$')
    @route(r'^(?P<week>[0-9]{4}-W[0-9]{2})/$')
    def week(self, request, week=None):
        context = self.get_context(request)
        context['scope'] = scopes.Week
        return TemplateResponse(
            request,
            self.get_template(request),
            context
        )

    @route(r'^month/$')
    @route(r'^(?P<month>[0-9]{4}-M[0-9]{2})/$')
    def month(self, request, month=None):
        context = self.get_context(request)
        context['scope'] = scopes.Month
        return TemplateResponse(
            request,
            self.get_template(request),
            context
        )

    @route(r'^quarter/$')
    @route(r'^(?P<quarter>[0-9]{4}-Q[0-4])/$')
    def quarter(self, request, quarter=None):
        context = self.get_context(request)
        context['scope'] = scopes.Quarter
        return TemplateResponse(
            request,
            self.get_template(request),
            context
        )

    @route(r'^year/$')
    @route(r'^(?P<year>[0-9]{4})/$')
    def year(self, request, year=None):
        context = self.get_context(request)
        context['scope'] = scopes.Year
        return TemplateResponse(
            request,
            self.get_template(request),
            context
        )
