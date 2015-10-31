from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class ConnectedView(TemplateView):
    template_name = 'connected/index.html'
