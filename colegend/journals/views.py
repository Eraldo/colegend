from calendar import monthrange

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView, TemplateView
from django.utils.translation import ugettext_lazy as _

from colegend.core.views import RolesRequiredMixin, OwnerRequiredMixin
from colegend.dayentries.models import DayEntry
from colegend.journals.monthentries.models import MonthEntry
from colegend.journals.weekentries.models import WeekEntry
from .models import Journal, JournalPage
from .forms import JournalForm, DatePickerForm


class JournalMixin(object):
    model = Journal
    form_class = JournalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = JournalPage.objects.first()
        return context


class JournalIndexView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        self.url = reverse('journals:day', kwargs={'date': timezone.now().date()})
        return super().get_redirect_url(*args, **kwargs)


class JournalListView(LoginRequiredMixin, RolesRequiredMixin, JournalMixin, ListView):
    template_name = 'journals/list.html'
    context_object_name = 'journals'
    required_roles = ['admin']


class JournalCreateView(LoginRequiredMixin, RolesRequiredMixin, JournalMixin, CreateView):
    template_name = 'journals/create.html'
    required_roles = ['admin']


class JournalDetailView(LoginRequiredMixin, OwnerRequiredMixin, JournalMixin, DetailView):
    template_name = 'journals/detail.html'


class JournalUpdateView(LoginRequiredMixin, OwnerRequiredMixin, JournalMixin, UpdateView):
    template_name = 'journals/update.html'


class JournalDeleteView(LoginRequiredMixin, RolesRequiredMixin, JournalMixin, DeleteView):
    template_name = 'journals/delete.html'
    required_roles = ['admin']

    def get_success_url(self):
        object = self.get_object()
        return object.index_url


class JournalSettingsView(LoginRequiredMixin, OwnerRequiredMixin, JournalMixin, UpdateView):
    template_name = 'journals/settings.html'

    def get_success_url(self):
        return self.get_object().index_url

    def post(self, request, *args, **kwargs):
        reset = request.POST.get('reset')
        if reset:
            journal = self.get_object()
            journal.reset()
            messages.success(request, _('Journal defaults have been restored.'))
            return redirect('.')
        return super().post(request, *args, **kwargs)


class JournalDayView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/day.html'

    def get_date(self):
        date_string = self.kwargs.get('date')
        if date_string:
            return parse_date(date_string)
        else:
            today = timezone.now().date()
            return today

    def get_entry(self, date=None):
        date = date or self.get_date()
        user = self.request.user
        try:
            return user.journal.dayentries.get(date=date)
        except DayEntry.DoesNotExist:
            return None

    def get_object(self, queryset=None):
        return self.get_entry()

    def get(self, request, *args, **kwargs):
        date = self.request.GET.get('date')
        if date:
            return redirect('journals:day', date)
        return super().get(request, *args, **kwargs)

    def get_next_url(self):
        date = self.get_date()
        next_date = date + timezone.timedelta(days=1)
        return reverse('journals:day', kwargs={'date': next_date})

    def get_previous_url(self):
        date = self.get_date()
        previous_date = date - timezone.timedelta(days=1)
        return reverse('journals:day', kwargs={'date': previous_date})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        dayentry = self.get_object()
        context['dayentry'] = dayentry

        date = self.get_date()
        context['date'] = date

        context['datepickerform'] = DatePickerForm(initial={'date': date})

        # previous and next button context
        context['next_url'] = self.get_next_url()
        context['previous_url'] = self.get_previous_url()
        create_url = reverse('dayentries:create')
        context['create_url'] = '{}?date={}'.format(create_url, date)
        context['settings_url'] = reverse('journals:settings', kwargs={'pk': user.journal.pk})

        # Add the users daily outcomes
        outcomes = user.outcomes.all()
        context['scheduled_outcomes'] = outcomes.scheduled(date=date)
        context['deadlined_outcomes'] = outcomes.deadlined(date=date)
        return context


class JournalWeekView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/week.html'

    def get_date(self):
        date_string = self.kwargs.get('date')
        if date_string:
            return parse_date(date_string)
        else:
            today = timezone.now().date()
            return today

    def get_dates(self):
        monday = self.get_monday()
        sunday = self.get_sunday()
        return '{} - {}'.format(monday, sunday)

    def get_entry(self, date=None):
        date = date or self.get_date()
        user = self.request.user
        try:
            return user.journal.dayentries.get(date=date)
        except DayEntry.DoesNotExist:
            return None

    def get_object(self, queryset=None):
        return self.get_entry()

    def get(self, request, *args, **kwargs):
        date = self.request.GET.get('date')
        if date:
            return redirect('journals:week', date)
        return super().get(request, *args, **kwargs)

    def get_next_url(self):
        date = self.get_date()
        next_date = date + timezone.timedelta(days=7)
        return reverse('journals:week', kwargs={'date': next_date})

    def get_previous_url(self):
        date = self.get_date()
        previous_date = date - timezone.timedelta(days=7)
        return reverse('journals:week', kwargs={'date': previous_date})

    def get_monday(self, date=None):
        date = self.get_date()
        monday = date - timezone.timedelta(days=date.weekday())
        return monday

    def get_sunday(self, date=None):
        monday = self.get_monday()
        sunday = monday + timezone.timedelta(days=6)
        return sunday

    def get_week_dates(self):
        one_day = timezone.timedelta(1)
        monday = self.get_monday()
        tuesday = monday + one_day
        wednesday = tuesday + one_day
        thursday = wednesday + one_day
        friday = thursday + one_day
        saturday = friday + one_day
        sunday = saturday + one_day
        return [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Context for the this week's entries.
        dates = self.get_week_dates()
        days = []
        for date in dates:
            days.append({
                'date': date,
                'entry': self.get_entry(date)
            })
        context['days'] = days

        date = self.get_date()
        context['datepickerform'] = DatePickerForm(initial={'date': date})

        # Previous and next button context.
        context['next_url'] = self.get_next_url()
        context['previous_url'] = self.get_previous_url()
        context['settings_url'] = reverse('journals:settings', kwargs={'pk': user.journal.pk})

        date = self.get_date()
        context['date'] = date
        dates = self.get_dates()
        context['dates'] = dates

        weeknumber = date.isocalendar()[1]
        context['weeknumber'] = weeknumber
        weekentry = WeekEntry.objects.owned_by(user).filter(year=date.year, week=weeknumber)
        if weekentry:
            context['weekentry'] = weekentry.first()

        context['settings_url'] = reverse('journals:settings', kwargs={'pk': user.journal.pk})

        # Add the users daily outcomes
        outcomes = user.outcomes.all()
        start, end = dates.split(' - ')
        context['scheduled_outcomes'] = outcomes.scheduled(date=start, end=end)
        context['deadlined_outcomes'] = outcomes.deadlined(date=start, end=end)
        return context


class JournalMonthView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/month.html'

    def get_date(self):
        date_string = self.kwargs.get('date')
        if date_string:
            return parse_date(date_string)
        else:
            today = timezone.now().date()
            return today

    def get_dates(self):
        first_day = self.get_first_day()
        last_day = self.get_last_day()
        return '{} - {}'.format(first_day, last_day)

    def get_entry(self, date=None):
        date = date or self.get_date()
        user = self.request.user
        try:
            return user.journal.weekentries.get(year=date.year, week=date.isocalendar()[1])
        except WeekEntry.DoesNotExist:
            return None

    def get_object(self, queryset=None):
        return self.get_entry()

    def get(self, request, *args, **kwargs):
        date = self.request.GET.get('date')
        if date:
            return redirect('journals:month', date)
        return super().get(request, *args, **kwargs)

    def get_next_url(self):
        date = self.get_date()
        days_in_month = monthrange(date.year, date.month)[1]
        next_date = date + timezone.timedelta(days=days_in_month)
        return reverse('journals:month', kwargs={'date': next_date})

    def get_previous_url(self):
        date = self.get_date()
        days_in_month = monthrange(date.year, date.month)[1]
        previous_date = date - timezone.timedelta(days=days_in_month)
        return reverse('journals:month', kwargs={'date': previous_date})

    def get_first_day(self, date=None):
        date = self.get_date()
        first_day = date - timezone.timedelta(days=date.day-1)
        return first_day

    def get_last_day(self, date=None):
        first_day = self.get_first_day()
        days_in_month = monthrange(first_day.year, first_day.month)[1]
        last_day = first_day + timezone.timedelta(days_in_month-1)
        return last_day

    def get_month_weeks(self):
        one_week = timezone.timedelta(7)
        weeks = []
        day = self.get_first_day()
        month = day.month
        while day.month == month:
            weeks.append('{year}-W{week}'.format(year=day.year, week=day.isocalendar()[1]))
            day += one_week
        return weeks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Context for the this month's entries.
        weeks_strings = self.get_month_weeks()
        weeks = []
        for week_string in weeks_strings:
            date = timezone.datetime.strptime('{}-1'.format(week_string), "%Y-W%W-%w").date()
            weeks.append({
                'date': date,
                'entry': self.get_entry(date)
            })
        context['weeks'] = weeks

        date = self.get_date()
        context['datepickerform'] = DatePickerForm(initial={'date': date})

        # # Previous and next button context.
        context['next_url'] = self.get_next_url()
        context['previous_url'] = self.get_previous_url()
        context['settings_url'] = reverse('journals:settings', kwargs={'pk': user.journal.pk})

        date = self.get_date()
        context['date'] = date
        dates = self.get_dates()
        context['dates'] = dates
        #
        monthnumber = date.month
        context['monthnumber'] = monthnumber
        monthentry = MonthEntry.objects.owned_by(user).filter(year=date.year, month=monthnumber)
        if monthentry:
            context['monthentry'] = monthentry.first()

        context['settings_url'] = reverse('journals:settings', kwargs={'pk': user.journal.pk})

        # Add the users daily outcomes
        outcomes = user.outcomes.all()
        start, end = dates.split(' - ')
        context['scheduled_outcomes'] = outcomes.scheduled(date=start, end=end)
        context['deadlined_outcomes'] = outcomes.deadlined(date=start, end=end)
        return context


class JournalSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        text = self.request.GET.get('text')
        if text:
            context['text'] = text
            user = self.request.user
            days = DayEntry.objects.owned_by(user).filter(
                Q(keywords__icontains=text) | Q(content__icontains=text) | Q(locations__icontains=text) | Q(tags__name__icontains=text)
            ).distinct()
            context['days'] = days
            weeks = WeekEntry.objects.owned_by(user).filter(
                Q(keywords__icontains=text) | Q(content__icontains=text) | Q(tags__name__icontains=text)
            ).distinct()
            context['weeks'] = weeks
            months = MonthEntry.objects.owned_by(user).filter(
                Q(keywords__icontains=text) | Q(content__icontains=text) | Q(tags__name__icontains=text)
            ).distinct()
            context['months'] = months
        return context
