from django.conf.urls import patterns, url
from dojo.views import DojoView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        DojoView.as_view(),
        name='home'),
)
