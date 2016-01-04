from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class GameIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'
