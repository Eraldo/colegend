from django.shortcuts import render
from django.views.generic import ListView
from features.models import Feature

__author__ = 'eraldo'


class FeatureListView(ListView):
    model = Feature
    fields = ['name', 'description', 'date_published']