from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class AboutView(TemplateView):
    template_name = "about/about.html"
