from django.conf.urls import patterns, url
from website.views import TestView, SearchView

__author__ = 'eraldo'


urlpatterns = patterns('',
    url(r'^search/$',
        SearchView.as_view(),
        name='search'),
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
    )