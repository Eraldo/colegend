from braces.views import LoginRequiredMixin
from django.views.generic import ListView

from cards.models import Card


class CardListView(LoginRequiredMixin, ListView):
    template_name = 'cards/list.html'
    model = Card
    context_object_name = 'cards'
