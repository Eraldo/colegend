from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from features.models import Feature

__author__ = 'eraldo'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['feature'] = Feature.objects.first()
        return context
