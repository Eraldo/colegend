from django.shortcuts import render
from django.views.generic import ListView
from features.models import Feature
from lib.views import get_icon

__author__ = 'eraldo'


class FeatureListView(ListView):
    model = Feature
    fields = ['name', 'description', 'date_published']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icon"] = get_icon("road")
        return context
