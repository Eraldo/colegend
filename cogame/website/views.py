from django.contrib import messages
from django.views.generic import TemplateView

__author__ = 'eraldo'


class TestView(TemplateView):
    template_name = "website/test.html"

    def get(self, request, *args, **kwargs):
        message = "test1"
        messages.add_message(request, messages.INFO, message)
        message = "test2"
        messages.add_message(request, messages.INFO, message)
        return super(TestView, self).get(request, *args, **kwargs)