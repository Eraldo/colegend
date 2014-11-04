from django.conf.urls import patterns, url
from meetings.views import GatheringsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        GatheringsView.as_view(),
        name='gatherings'),
)
