from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnerRequiredMixin
from colegend.dayentries.models import DayEntry
from colegend.journals.weekentries.utils import get_current_year, get_current_week
from .forms import WeekEntryForm
from .models import WeekEntry


class WeekEntryMixin(object):
    """
    Default attributes and methods for weekentry related views.
    """
    model = WeekEntry
    form_class = WeekEntryForm

    def get_form(self):
        form = super().get_form()
        # limit tag choices to owned tags
        user = self.request.user
        form.fields['tags'].queryset = user.tags.all()
        return form


class WeekEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'weekentries:list'


class WeekEntryListView(LoginRequiredMixin, WeekEntryMixin, ListView):
    template_name = 'weekentries/list.html'
    context_object_name = 'weekentries'


class WeekEntryCreateView(LoginRequiredMixin, WeekEntryMixin, CreateView):
    template_name = 'weekentries/create.html'

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

        # Creation year/week is given or curreny year/week as default.
        year = self.request.GET.get('year', get_current_year())
        initial['year'] = year
        week = self.request.GET.get('week', get_current_week())
        initial['week'] = week

        # default content
        initial['content'] = journal.content_template or ''

        start = timezone.datetime.strptime('{}-W{}-1'.format(year, week), "%Y-W%W-%w")
        end = start + timezone.timedelta(days=6)
        if start and end:
            days = DayEntry.objects.owned_by(user).filter(date__range=[start, end])
            if days:
                tags = days.values_list('tags', flat=True)
                initial['tags'] = set(tags)

        return initial


class WeekEntryDetailView(LoginRequiredMixin, OwnerRequiredMixin, WeekEntryMixin, DetailView):
    template_name = 'weekentries/detail.html'


class WeekEntryUpdateView(LoginRequiredMixin, OwnerRequiredMixin, WeekEntryMixin, UpdateView):
    template_name = 'weekentries/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs


class WeekEntryDeleteView(LoginRequiredMixin, OwnerRequiredMixin, WeekEntryMixin, DeleteView):
    template_name = 'weekentries/delete.html'

    def get_success_url(self):
        weekentry = self.get_object()
        return reverse('journals:week', kwargs={'date': weekentry.date})
