from django.conf.urls import patterns, url
from meetings.views import MeetingsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        MeetingsView.as_view(),
        name='meetings'),
)
