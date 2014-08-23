from django.conf.urls import patterns, url
from website.views import TestView, SearchResultsView, AboutView, HomeView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^about/$',
        AboutView.as_view(),
        name='about'),
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^search/$',
        SearchResultsView.as_view(),
        name='search'),
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
