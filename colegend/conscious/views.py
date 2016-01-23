from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ConsciousView(LoginRequiredMixin, TemplateView):
    template_name = 'conscious/conscious.html'
