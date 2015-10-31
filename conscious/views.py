from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ConsciousView(LoginRequiredMixin, TemplateView):
    template_name = 'conscious/index.html'
