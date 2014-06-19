from django.conf.urls import patterns, url
from commands.views import CommandsView

__author__ = 'eraldo'


urlpatterns = patterns('',
    url(r'^$',
        CommandsView.as_view(),
        name='commands'),
    )