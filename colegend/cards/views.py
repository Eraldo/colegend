from annoying.functions import get_object_or_None
from django.views.generic import ListView, DetailView
from cards.models import Card, Deck
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class CardMixin(ActiveUserRequiredMixin):
    model = Card
    icon = "card"
    tutorial = "Cards"


class CardPickerView(CardMixin, ListView):
    template_name = "cards/card_picker.html"
    model = Deck


class CardShowView(CardMixin, DetailView):
    template_name = "cards/card_show.html"
