from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from colegend.cards.forms import CardForm
from colegend.cards.models import Card
from colegend.core.views import RolesRequiredMixin


class CardListView(LoginRequiredMixin, RolesRequiredMixin, ListView):
    template_name = 'cards/list.html'
    model = Card
    context_object_name = 'cards'
    required_roles = ['manager']


class CardCreateView(LoginRequiredMixin, RolesRequiredMixin, CreateView):
    template_name = 'cards/create.html'
    model = Card
    form_class = CardForm
    required_roles = ['admin']


class CardDetailView(LoginRequiredMixin, RolesRequiredMixin, DetailView):
    template_name = 'cards/detail.html'
    model = Card
    required_roles = ['manager']


class CardUpdateView(LoginRequiredMixin, RolesRequiredMixin, UpdateView):
    template_name = 'cards/update.html'
    model = Card
    form_class = CardForm
    required_roles = ['manager']


class CardDeleteView(LoginRequiredMixin, RolesRequiredMixin, DeleteView):
    template_name = 'cards/delete.html'
    model = Card
    required_roles = ['admin']
