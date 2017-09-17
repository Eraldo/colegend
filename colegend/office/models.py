from enum import Enum

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from django.utils.dateparse import parse_date
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase, TimeStampedBase
from colegend.journals import scopes
from colegend.journals.forms import DatePickerForm
from colegend.journals.scopes import Day, Week, Month, Year
from colegend.outcomes.models import Outcome


class Status(Enum):
    FUTURE = 'future'
    WAITING = 'waiting'
    CURRENT = 'current'
    DONE = 'done'
    CANCELED = 'canceled'


DAY = 'day'
WEEK = 'week'
MONTH = 'month'
YEAR = 'year'
SCOPE_CHOICES = (
    (DAY, _('day')),
    (WEEK, _('week')),
    (MONTH, _('month')),
    (YEAR, _('year')),
)


# class FocusOutcome(TimeStampedBase):
#     focus = models.ForeignKey(Focus, on_delete=models.CASCADE)
#     outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE)
#     priority = models.IntegerField(default=1)


class Focus(OwnedBase, TimeStampedBase):
    scope = models.CharField(
        _('scope'),
        choices=SCOPE_CHOICES,
        default=DAY,
        max_length=5,
    )
    start = models.DateField(
        _('start'),
    )
    end = models.DateField(
        _('end'),
        blank=True
    )

    # outcomes = models.ManyToManyField(
    #     to=Outcome,
    #     through=FocusOutcome
    # )

    outcome_1 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='focus_1',
    )

    outcome_2 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='focus_2',
    )

    outcome_3 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='focus_3',
    )

    outcome_4 = models.ForeignKey(
        to=Outcome,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='focus_4',
    )

    def get_scope(self):
        scope_map = {
            DAY: Day,
            WEEK: Week,
            MONTH: Month,
            YEAR: Year,
        }
        return scope_map.get(self.scope)(self.start)

    @property
    def outcomes(self):
        outcomes = [self.outcome_1, self.outcome_2, self.outcome_3, self.outcome_4]
        return [outcome for outcome in outcomes if outcome]

    class Meta:
        verbose_name = _('Focus outcomes')
        verbose_name_plural = _('Focus Outcomes')
        unique_together = ['owner', 'scope', 'start']
        ordering = ['start']
        default_related_name = 'focuses'

    def __str__(self):
        return "{}'s {} focus outcomes {}".format(self.owner, self.get_scope_display(), self.start)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Creation.
            # Adapting start and end dates to scope.
            scope = self.get_scope()
            self.start = scope.start
            self.end = scope.end
        super().save(*args, **kwargs)


class OfficePage(Page):
    template = 'office/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['AgendaPage', 'ActionPage', 'InboxPage', 'OutcomesPage']


class AgendaPage(RoutablePageMixin, Page):
    template = 'office/agenda.html'

    parent_page_types = ['OfficePage']
    subpage_types = []

    def get_scope(self, request):
        name = request.session.get('scope', scopes.Day().name)
        for scope in scopes.all:
            if scope().name == name:
                return scope(self.get_date(request))
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

        # set the date to the user requested date
        date_request = request.GET.get('date')
        if date_request:
            date = self.set_date(request, date_request)
        date = self.get_date(request)
        context['date'] = date
        context['datepickerform'] = DatePickerForm(initial={'date': date})

        scope_request = request.GET.get('scope')
        if scope_request:
            scope = self.set_scope(request, scope_request)
        scope = self.get_scope(request)
        context['scope'] = scope

        update = request.GET.get('update')
        if update:
            context['update'] = True

        user = request.user
        if request.user.is_authenticated:
            # focus
            try:
                focus = user.focuses.get(scope=scope.name, start=date)
            except Focus.DoesNotExist:
                focus = Focus.objects.none()
            if focus:
                context['focus_outcomes'] = focus.outcomes

            # form
            focus_outcomes_form = self.get_focus_form(user=user, scope=scope)
            context['focus_outcomes_form'] = focus_outcomes_form

            # scheduled
            context['scheduled_outcomes'] = user.outcomes.filter(date=date) | user.outcomes.filter(deadline=date)

            # experience
            context['experience'] = user.experience.total(app='office')
        return context

    def __str__(self):
        return self.title

    def get_focus_form(self, user, scope, data=None):
        from colegend.office.forms import FocusForm
        try:
            instance = user.focuses.get(scope=scope.name, start=scope.start)
        except Focus.DoesNotExist:
            instance = Focus.objects.none()
        if instance:
            form = FocusForm(owner=user, instance=instance, data=data)
        else:
            initial = {'owner': user, 'scope': scope.name, 'start': scope.start}
            form = FocusForm(owner=user, initial=initial, data=data)
        return form

    @route(r'^form/$')
    def focus_form(self, request):
        context = self.get_context(request)
        submitted = request.POST.get('save')
        user = request.user
        if submitted:
            form = self.get_focus_form(user=user, scope=context['scope'], data=request.POST)
            if form.is_valid():
                new = not form.instance.pk
                form.save()

                if new:
                    # Adding experience if setting for today or tomorrow.
                    focus = form.instance
                    if focus.scope == DAY:
                        today = timezone.localtime(timezone.now()).date()
                        tomorrow = today + timezone.timedelta(days=1)
                        if focus.start == today or focus.start == tomorrow:
                            app = 'office'
                            level = 0
                            amount = 1
                            user.experience.create(owner=user, app=app, level=level, amount=amount)
                            message = '+{amount} {app} EXP'.format(amount=amount, app=app)
                            messages.success(request, message)
                            # TODO: Adding higher scopes experience
                return redirect(self.url)
            else:
                context['focus_outcomes_form'] = form
        context['show_update_form'] = True
        return TemplateResponse(
            request,
            self.get_template(request),
            context,
        )


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
