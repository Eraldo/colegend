from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from colegend.cards.models import Card


class CardListView(LoginRequiredMixin, ListView):
    template_name = 'cards/list.html'
    model = Card
    context_object_name = 'cards'


class CardDetailView(LoginRequiredMixin, DetailView):
    template_name = 'cards/detail.html'
    model = Card


class CardUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'cards/update.html'
    model = Card
