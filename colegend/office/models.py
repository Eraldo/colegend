from django.db import models
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.dateparse import parse_date
from wagtail.wagtailcore.models import Page
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase
from colegend.journals import scopes
from colegend.journals.forms import DatePickerForm
from colegend.outcomes.models import Outcome

DAY = 1
WEEK = 2
MONTH = 3
YEAR = 4
SCOPE_CHOICES = (
    (DAY, _('day')),
    (WEEK, _('week')),
    (MONTH, _('month')),
    (YEAR, _('year')),
)


class Focus(OwnedBase):
    scope = models.PositiveSmallIntegerField(
        _('scope'),
        choices=SCOPE_CHOICES,
        default=DAY,
    )
    start = models.DateField()
    outcomes = models.ManyToManyField(
        to=Outcome,
        related_name='focus',
    )

    class Meta:
        verbose_name = _('Focus outcomes')
        verbose_name_plural = _('Focus Outcomes')
        unique_together = ['owner', 'scope', 'start']
        ordering = ['start']
        default_related_name = 'focuses'

    def __str__(self):
        return "{}'s {} focus outcomes {}".format(self.owner, self.get_scope_display(), self.start)


class OfficePage(Page):
    template = 'office/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['AgendaPage', 'ActionPage', 'InboxPage', 'OutcomesPage']


class AgendaPage(Page):
    template = 'office/agenda.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_scope(self, request):
        name = request.session.get('scope', scopes.Day().name)
        for scope in scopes.all:
            if scope().name == name:
                return scope
        raise ValueError('Scope "{0}" not found.'.format(name))

    def set_scope(self, request, name):
        if isinstance(name, str):
            request.session['scope'] = name
            return self.get_scope(request)
        raise ValueError('Scope needs to be a string to be stored locally.')

    def get_date(self, request):
        date = request.session.get('date', timezone.localtime(timezone.now()).date())
        date = parse_date(str(date))
        return date

    def set_date(self, request, date):
        if not isinstance(date, str):
            date = str(date)
        request.session['date'] = date
        return self.get_date(request)


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['scopes'] = scopes.all
        # self.set_scope(request, scopes.Day)
        scope = self.get_scope(request)
        context['scope'] = scopes.Day()
        date = scopes.Day().date
        context['date'] = date
        context['datepickerform'] = DatePickerForm(initial={'date': date})

        user = request.user
        if request.user.is_authenticated:
            # focus
            print(date)
            try:
                focus = user.focuses.get(scope=DAY, start=date)
            except Focus.DoesNotExist:
                focus = Focus.objects.none()
            if focus:
                context['focus_outcomes'] = focus.outcomes.all()

            # scheduled
            context['scheduled_outcomes'] = user.outcomes.filter(date=date) | user.outcomes.filter(deadline=date)
        return context

    def __str__(self):
        return self.title


class ActionPage(Page):
    template = 'office/action.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class InboxPage(Page):
    template = 'office/inbox.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class OutcomesPage(Page):
    template = 'office/outcomes.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
