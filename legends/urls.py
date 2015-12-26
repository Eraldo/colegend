from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import LegendDetailView, LegendListView

__author__ = 'Eraldo Energy'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='list', permanent=False),
        name='index'),
    url(r'^list/$',
        LegendListView.as_view(),
        name='list'),
    url(r'^legend/$',
        LegendDetailView.as_view(),
        name='legend'),
    url(r'^(?P<owner>[\w.@+-]+)/$',
        LegendDetailView.as_view(),
        name='detail'),
)
