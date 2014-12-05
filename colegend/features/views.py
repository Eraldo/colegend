from django.views.generic import ListView
from features.models import Feature

__author__ = 'eraldo'


class FeatureListView(ListView):
    model = Feature
    fields = ['name', 'description', 'date_published']
    icon = "feature"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
