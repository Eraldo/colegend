from django.conf.urls import url
from .views import ConnectedView, VirtualRoomView, GuidelinesView, GuidelinesIntroductionView, ChatView, \
    ChatIntroductionView, ChatInvitationView

__author__ = 'eraldo'

urlpatterns = [
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
    url(r'^virtual-room/$',
        VirtualRoomView.as_view(),
        name='virtual-room'),
]
