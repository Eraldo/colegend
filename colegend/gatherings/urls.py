from django.conf.urls import patterns, url
from gatherings.views import GatheringsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        GatheringsView.as_view(),
        name='gatherings'),
)
