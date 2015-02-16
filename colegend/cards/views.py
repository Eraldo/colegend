from django.views.generic import ListView, DetailView
from cards.models import Card
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class CardMixin(ActiveUserRequiredMixin):
    model = Card
    icon = "card"
    tutorial = "Cards"


class CardPickerView(CardMixin, ListView):
    template_name = "cards/card_picker.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('?')


class CardShowView(CardMixin, DetailView):
    template_name = "cards/card_show.html"
