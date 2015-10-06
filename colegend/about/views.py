from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class IndexView(TemplateView):
    template_name = "about/index.html"
