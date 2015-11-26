from django.conf.urls import patterns, url
from .views import ConnectedView, VirtualRoomView, GuidelinesView, GuidelinesIntroductionView, ChatView, \
    ChatIntroductionView, ChatInvitationView, GuideIntroductionView, GuideView

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
    url(r'^chat/introduction/$',
        ChatIntroductionView.as_view(),
        name='chat-introduction'),
    url(r'^chat/invitation/$',
        ChatInvitationView.as_view(),
        name='chat-invitation'),
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    url(r'^guide/introduction/$',
        GuideIntroductionView.as_view(),
        name='guide-introduction'),
    url(r'^guide/$',
        GuideView.as_view(),
        name='guide'),
    url(r'^virtual-room/$',
        VirtualRoomView.as_view(),
        name='virtual-room'),
)
