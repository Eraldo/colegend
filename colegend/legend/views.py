from django.contrib.auth import get_user_model

# Create your views here.
from django.views.generic import TemplateView
from legend.models import Block
from lib.views import ActiveUserRequiredMixin
from tutorials.models import get_tutorial

__author__ = 'eraldo'


class LegendMixin(ActiveUserRequiredMixin):
    icon = "legend"


class LegendView(LegendMixin, TemplateView):
    template_name = "legend/legend.html"

    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        try:
            introduction = Block.objects.get(name="Introduction").description
        except Block.DoesNotExist:
            introduction = None
        context['introduction'] = introduction
        context['candidates'] = get_user_model().objects.accepted().exclude(pk__lt=4)
        context['tutorial'] = get_tutorial("Legend")
        return context
