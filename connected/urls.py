from django.conf.urls import patterns, url

from .views import ConnectedView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ConnectedView.as_view(),
        name='index'),
)
