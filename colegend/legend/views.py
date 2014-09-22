from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from legend.models import Block
from lib.views import ActiveUserRequiredMixin


class QuoteMixin(ActiveUserRequiredMixin):
    pass


class LegendView(QuoteMixin, TemplateView):
    template_name = "legend/legend.html"

    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        try:
            introduction = Block.objects.get(name="Introduction").description
        except Block.DoesNotExist:
            introduction = None
        context['introduction'] = introduction
        context['candidates'] = get_user_model().objects.accepted()
        return context
