from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

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
