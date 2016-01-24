from django.contrib.auth.mixins import LoginRequiredMixin
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


class DayEntryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dayentries/detail.html'
    model = DayEntry


class DayEntryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dayentries/update.html'
    model = DayEntry
    form_class = DayEntryForm


class DayEntryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'dayentries/delete.html'
    model = DayEntry
