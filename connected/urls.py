from django.conf.urls import patterns, url
from .views import ConnectedView, VirtualRoomView, GuidelinesView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ConnectedView.as_view(),
        name='index'),
    url(r'^virtual-room/$',
        VirtualRoomView.as_view(),
        name='virtual-room'),
    url(r'^guidelines/$',
        GuidelinesView.as_view(),
        name='guidelines'),
)
