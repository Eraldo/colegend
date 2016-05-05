from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class SandboxView(TemplateView):
    template_name = "sandbox/index.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Test page loaded")
        return super().get(request, *args, **kwargs)

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context['user'] = self.request.u
