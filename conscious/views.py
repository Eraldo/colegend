from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ConsciousView(LoginRequiredMixin, TemplateView):
    template_name = 'conscious/conscious.html'


class OuterCall(LoginRequiredMixin, TemplateView):
    template_name = 'conscious/outer-call.html'
