from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

__author__ = 'eraldo'


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect("about")
        return super().get(request, *args, **kwargs)


class TestView(TemplateView):
    template_name = "pages/test.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Test page loaded")
        return super().get(request, *args, **kwargs)
