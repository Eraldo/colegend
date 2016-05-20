from django.contrib import messages

# Create your views here.
from django.views.generic import TemplateView

from colegend.cards.models import Card


class SandboxView(TemplateView):
    template_name = "sandbox/index.html"

    def get(self, request, *args, **kwargs):
        messages.success(request, "Test page loaded")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card'] = Card.objects.first()
        return context
