from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ContinuousView(LoginRequiredMixin, TemplateView):
    template_name = 'continuous/index.html'
