from django.conf.urls import patterns, url
from website.views import TestView, SearchView, AboutView, HomeView, ChatView, MapView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^about/$',
        AboutView.as_view(),
        name='about'),
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^map/$',
        MapView.as_view(),
        name='map'),
    url(r'^search/$',
        SearchView.as_view(),
        name='search'),
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
