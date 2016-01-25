from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

__author__ = 'eraldo'


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        # Redirect anonymous users to the about page.
        if not user.is_authenticated():
            return redirect("about")
        # Redirect if prologue is not completed.
        if not user.has_checkpoint('prologue'):
            return redirect("story:prologue")
        return super().get(request, *args, **kwargs)


class JoinView(TemplateView):
    template_name = "home/join.html"


class TestView(TemplateView):
    template_name = "pages/test.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Test page loaded")
        return super().get(request, *args, **kwargs)

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context['user'] = self.request.u
