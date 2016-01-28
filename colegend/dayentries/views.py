from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from .models import DayEntry
from .forms import DayEntryForm


class DayEntryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'dayentries:list'


class DayEntryListView(LoginRequiredMixin, ListView):
    template_name = 'dayentries/list.html'
    model = DayEntry
    context_object_name = 'dayentries'


class DayEntryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dayentries/create.html'
    model = DayEntry
    form_class = DayEntryForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['journal'] = self.request.user.journal
        date = self.request.GET.get('date')
        if date:
            initial['date'] = date
        return initial


class DayEntryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dayentries/detail.html'
    model = DayEntry


class DayEntryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dayentries/update.html'
    model = DayEntry
    form_class = DayEntryForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['journal'] = self.request.user.journal
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['journal'] = self.request.user.journal
        return initial


class DayEntryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dayentries/delete.html'
    model = DayEntry

    def get_success_url(self):
        dayentry = self.get_object()
        return reverse('journals:day', kwargs={'date': dayentry.date})
