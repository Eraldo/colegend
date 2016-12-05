from calendar import monthrange

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnerRequiredMixin
from colegend.dayentries.models import DayEntry
from colegend.journals.monthentries.utils import get_current_year, get_current_month
from .forms import MonthEntryForm
from .models import MonthEntry


class MonthEntryMixin(object):
    """
    Default attributes and methods for monthentry related views.
    """
    model = MonthEntry
    form_class = MonthEntryForm

    def get_form(self):
        form = super().get_form()
        # limit tag choices to owned tags
        user = self.request.user
        form.fields['tags'].queryset = user.tags.all()
        return form


class MonthEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'monthentries:list'


class MonthEntryListView(LoginRequiredMixin, MonthEntryMixin, ListView):
    template_name = 'monthentries/list.html'
    context_object_name = 'monthentries'


class MonthEntryCreateView(LoginRequiredMixin, MonthEntryMixin, CreateView):
    template_name = 'monthentries/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs

    def get_initial(self):
        initial = super().get_initial()

        # Set the default owned journal.
        user = self.request.user
        journal = user.journal
        initial['journal'] = journal

        # Creation year/month is given or curreny year/month as default.
        year = self.request.GET.get('year', get_current_year())
        initial['year'] = year
        month = self.request.GET.get('month', get_current_month())
        initial['month'] = month

        # default content
        initial['content'] = journal.month_template or render_to_string('monthentries/template.md')

        # prefill tags
        start = timezone.datetime.strptime('{}-M{}'.format(year, month), "%Y-M%m")
        days_in_month = monthrange(int(year), int(month))[1]
        end = start + timezone.timedelta(days=days_in_month-1)
        if start and end:
            days = DayEntry.objects.owned_by(user).filter(date__range=[start, end])
            if days:
                tags = days.values_list('tags', flat=True)
                initial['tags'] = set(tags)

        return initial


class MonthEntryDetailView(LoginRequiredMixin, OwnerRequiredMixin, MonthEntryMixin, DetailView):
    template_name = 'monthentries/detail.html'


class MonthEntryUpdateView(LoginRequiredMixin, OwnerRequiredMixin, MonthEntryMixin, UpdateView):
    template_name = 'monthentries/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs


class MonthEntryDeleteView(LoginRequiredMixin, OwnerRequiredMixin, MonthEntryMixin, DeleteView):
    template_name = 'monthentries/delete.html'

    def get_success_url(self):
        monthentry = self.get_object()
        return reverse('journals:month', kwargs={'date': monthentry.date})
