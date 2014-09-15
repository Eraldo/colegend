from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from legend.models import Block


class LegendView(TemplateView):
    template_name = "legend/legend.html"

    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        context['introduction'] = Block.objects.get(name="Introduction").description
        return context
