from django.views.generic import TemplateView

__author__ = 'eraldo'


class HomeView(TemplateView):
    template_name = "home/home.html"