from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import RolesRequiredMixin
from .models import Donation
from .forms import DonationForm


class DonationMixin:
    """
    Default attributes and methods for donation related views.
    """
    model = Donation
    form_class = DonationForm


class DonationIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'donations:list'


class DonationListView(LoginRequiredMixin, DonationMixin, ListView):
    template_name = 'donations/list.html'
    context_object_name = 'donations'


class DonationCreateView(LoginRequiredMixin, RolesRequiredMixin, DonationMixin, CreateView):
    template_name = 'donations/create.html'
    required_roles = ['admin']


class DonationDetailView(LoginRequiredMixin, DonationMixin, DetailView):
    template_name = 'donations/detail.html'


class DonationUpdateView(LoginRequiredMixin, RolesRequiredMixin, DonationMixin, UpdateView):
    template_name = 'donations/update.html'
    required_roles = ['admin']


class DonationDeleteView(LoginRequiredMixin, RolesRequiredMixin, DonationMixin, DeleteView):
    template_name = 'donations/delete.html'
    required_roles = ['admin']

    def get_success_url(self):
        donation = self.get_object()
        return donation.index_url
