from django.conf.urls import patterns, url
from website.views import TestView

__author__ = 'eraldo'


urlpatterns = patterns('',
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
    )