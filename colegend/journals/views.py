from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.dateparse import parse_date
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView, TemplateView

from colegend.core.views import RolesRequiredMixin, OwnerRequiredMixin
from colegend.dayentries.models import DayEntry
from .models import Journal
from .forms import JournalForm


class JournalIndexView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        self.url = self.request.user.journal.get_absolute_url()
        return super().get_redirect_url(*args, **kwargs)


class JournalListView(LoginRequiredMixin, RolesRequiredMixin, ListView):
    template_name = 'journals/list.html'
    model = Journal
    context_object_name = 'journals'
    required_roles = ['admin']


class JournalCreateView(LoginRequiredMixin, RolesRequiredMixin, CreateView):
    template_name = 'journals/create.html'
    model = Journal
    form_class = JournalForm
    required_roles = ['admin']


class JournalDetailView(LoginRequiredMixin, OwnerRequiredMixin, DetailView):
    template_name = 'journals/detail.html'
    model = Journal


class JournalUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    template_name = 'journals/update.html'
    model = Journal
    form_class = JournalForm


class JournalDeleteView(LoginRequiredMixin, RolesRequiredMixin, DeleteView):
    template_name = 'journals/delete.html'
    model = Journal
    required_roles = ['admin']

    def get_success_url(self):
        object = self.get_object()
        return object.index_url()


class JournalDayView(LoginRequiredMixin, TemplateView):
    template_name = 'journals/day.html'

    def get(self, request, *args, **kwargs):
        date = self.request.GET.get('date')
        if date:
            return redirect('journals:day', date)
        return super().get(request, *args, **kwargs)

    def get_entry(self, date):
        if date:
            date = parse_date(date)
            user = self.request.user
            try:
                return user.journal.dayentries.get(date=date)
            except DayEntry.DoesNotExist:
                return None

    def get_object(self, queryset=None):
        # Check if date is provided.. if so use it..
        date = self.kwargs.get('date')
        return self.get_entry(date)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dayentry'] = self.get_object()
        return context
