from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ConnectedView(LoginRequiredMixin, TemplateView):
    template_name = 'connected/connected.html'
