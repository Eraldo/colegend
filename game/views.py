from braces.views import LoginRequiredMixin
from django.template.loader import render_to_string
from django.views.generic import TemplateView


class GameIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cards_data = [
            {
                'title': 'card 1',
                'content': 'Some text.',
                'source': 'http://lorempixel.com/400/200/cats/card/',
            },
            {
                'title': 'card 2 - blub',
                'content': 'Some more text.',
                'source': 'http://lorempixel.com/400/200/cats/card/',
            },
            {
                'title': 'card 2',
                'content': 'Some even longer text. Some even longer text. Some even longer text. Some even longer text.',
                'source': 'http://lorempixel.com/400/200/cats/card/',
            },
        ]
        cards = []
        template = 'game/widgets/card.html'
        for data in cards_data:
            card = render_to_string(template, data)
            cards.append(card)
        context['cards'] = cards
        return context
