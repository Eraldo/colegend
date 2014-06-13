from django.conf.urls import patterns, url
from home.views import HomeView

__author__ = 'eraldo'


urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    )