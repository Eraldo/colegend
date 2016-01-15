from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView, ListView
from django.utils.translation import ugettext as _

from cards.models import Card


class GameIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'games/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        game = user.game
        context['cards'] = game.hand.all()
        context['can_draw'] = game.can_draw
        context['completed'] = game.completed.count()
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        if 'draw' in post:
            game = request.user.game
            game.draw()
            return redirect('games:index')


class CompletedView(LoginRequiredMixin, ListView):
    template_name = 'games/completed.html'
    model = Card
    context_object_name = 'cards'

    def get_queryset(self):
        user = self.request.user
        return user.game.completed.all().reverse()


def complete_card(request, card):
    game = request.user.game
    if isinstance(card, str):
        card = game.get_card(card)
    game.complete_card(card)
    game.save()

    card_name = '{} card'.format(card)
    context = {'name': card_name, 'url': reverse('games:completed')}
    card_link = render_to_string('cards/widgets/link.html', context=context)
    success_message = _('Congratulations! You completed the {card_link}.').format(card_link=card_link)

    game_link = reverse('games:index')
    continue_message = _(
        'If you want you can continue to play the <a id="continue-game-button" href="{link}">game</a>.').format(
        link=game_link)
    message = '{}<br>{}'.format(success_message, continue_message)
    messages.success(request, mark_safe(message))
