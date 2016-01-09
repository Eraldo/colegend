from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView


class GameIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        game = user.game
        rendered_cards = []
        card_template = 'game/widgets/card.html'
        for card in game.hand.all():
            card_context = {
                'title': card.name,
                'content': card.content,
                'source': card.image.url if card.image else '',
            }
            rendered_card = render_to_string(card_template, card_context)
            rendered_cards.append(rendered_card)
        context['cards'] = rendered_cards
        context['can_draw'] = game.can_draw
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        if 'draw' in post:
            game = request.user.game
            game.draw()
            return redirect('game:index')
