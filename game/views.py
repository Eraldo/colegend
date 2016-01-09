from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView


class GameIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        game = user.game
        context['cards'] = game.hand.all()
        context['can_draw'] = game.can_draw
        return context

    def post(self, request, *args, **kwargs):
        post = request.POST
        if 'draw' in post:
            game = request.user.game
            game.draw()
            return redirect('game:index')
