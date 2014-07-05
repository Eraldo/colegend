from django.views.generic import TemplateView

__author__ = 'eraldo'


class TestView(TemplateView):
    template_name = "website/local_test.html"