from django.conf.urls import patterns, url
from .views import ConsciousView, OuterCall

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ConsciousView.as_view(),
        name='index'),
    url(r'^outer-call$',
        OuterCall.as_view(),
        name='outer-call'),
)
