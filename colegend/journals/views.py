from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import RolesRequiredMixin, OwnerRequiredMixin
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
        return self.get_object().get_index_url()
