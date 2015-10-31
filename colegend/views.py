from django.contrib import messages
from django.views.generic import TemplateView

__author__ = 'eraldo'


class TestPageView(TemplateView):
    template_name = "pages/test.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Test page loaded")
        return super().get(request, *args, **kwargs)
