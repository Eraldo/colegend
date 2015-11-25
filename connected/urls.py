from django.conf.urls import patterns, url
from .views import ConnectedView, VirtualRoomView, GuidelinesView, GuidelinesIntroductionView, ChatView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        ConnectedView.as_view(),
        name='index'),
    url(r'^guidelines/introduction/$',
        GuidelinesIntroductionView.as_view(),
        name='guidelines-introduction'),
    url(r'^guidelines/$',
        GuidelinesView.as_view(),
        name='guidelines'),
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    url(r'^virtual-room/$',
        VirtualRoomView.as_view(),
        name='virtual-room'),
)
