# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.urls import reverse
# from django.shortcuts import redirect
# from django.template.loader import render_to_string
# from django.utils.safestring import mark_safe
# from django.views.generic import TemplateView, ListView
# from django.utils.translation import ugettext as _
#
# from colegend.cards.models import Card
#
#
# class GameIndexView(LoginRequiredMixin, TemplateView):
#     template_name = 'games/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         game = user.game
#         context['cards'] = game.hand.all()
#         context['can_draw'] = game.can_draw
#         context['completed'] = game.completed.count()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         post = request.POST
#         if 'draw' in post:
#             user = request.user
#             game = user.game
#             card = game.draw()
#             checkpoint_name = '{} card'.format(str(card.name).lower())
#             user.add_checkpoint(name=checkpoint_name)
#             return redirect('games:index')
#
#
# class CompletedView(LoginRequiredMixin, ListView):
#     template_name = 'games/completed.html'
#     model = Card
#     context_object_name = 'cards'
#
#     def get_queryset(self):
#         user = self.request.user
#         return user.game.completed.all().reverse()
#
#
# def complete_card(request, card):
#     user = request.user
#     game = user.game
#     if isinstance(card, str):
#         card = game.get_card(card)
#     completed = game.complete_card(card)
#     if completed:
#         checkpoint_name = str(card.name).lower()
#         user.add_checkpoint(name=checkpoint_name)
#
#     card_name = '{} card'.format(card)
#     context = {'name': card_name, 'url': reverse('games:completed')}
#     card_link = render_to_string('cards/widgets/link.html', context=context)
#     success_message = _('Congratulations! You completed the {card_link}.').format(card_link=card_link)
#
#     game_link = reverse('games:index')
#     continue_message = _(
#         'If you want you can continue the <a id="continue-game-button" href="{link}">tutorial</a>.').format(
#         link=game_link)
#     message = '{}<br>{}'.format(success_message, continue_message)
#     messages.success(request, mark_safe(message))
