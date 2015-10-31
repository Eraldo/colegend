from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ContinuousView(TemplateView):
    template_name = 'continuous/index.html'
