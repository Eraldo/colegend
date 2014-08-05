from django.conf.urls import patterns, url
from website.views import TestView, SearchResultsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^search/$',
        SearchResultsView.as_view(),
        name='search'),
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)