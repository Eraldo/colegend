from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView, TemplateView

from colegend.core.views import RolesRequiredMixin, OwnerRequiredMixin
from colegend.dayentries.models import DayEntry
from .models import Journal
from .forms import JournalForm


class JournalMixin(object):
    model = Journal
    form_class = JournalForm


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


class JournalDayView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/day.html'

    def get_date(self):
        date_string = self.kwargs.get('date')
        if date_string:
            return parse_date(date_string)

    def get_entry(self, date):
        if date:
            user = self.request.user
            try:
                return user.journal.dayentries.get(date=date)
            except DayEntry.DoesNotExist:
                return None

    def get_object(self, queryset=None):
        date = self.get_date()
        return self.get_entry(date)

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

        dayentry = self.get_object()
        context['dayentry'] = dayentry

        date = self.get_date()
        context['date'] = date

        # previous and next button context
        context['next_url'] = self.get_next_url()
        context['previous_url'] = self.get_previous_url()
        create_url = reverse('dayentries:create')
        context['create_url'] = '{}?date={}'.format(create_url, date)
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

        # Context for the this week's entries.
        dates = self.get_week_dates()
        days = []
        for date in dates:
            days.append({
                'date': date,
                'entry': self.get_entry(date)
            })
        context['days'] = days

        # Previous and next button context.
        context['next_url'] = self.get_next_url()
        context['previous_url'] = self.get_previous_url()
        return context
