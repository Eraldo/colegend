from django.conf.urls import patterns, url

from .views import ConsciousView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ConsciousView.as_view(),
        name='index'),
)
