from django.conf.urls import url
from .views import ChatIntroductionView, ChatInvitationView, ChatView, VirtualRoomView

__author__ = 'eraldo'

app_name = 'chat'
urlpatterns = [
    url(r'^$',
        ChatView.as_view(),
        name='index'),
    url(r'^introduction/$',
        ChatIntroductionView.as_view(),
        name='introduction'),
    url(r'^invitation/$',
        ChatInvitationView.as_view(),
        name='invitation'),
    url(r'^room/$',
        VirtualRoomView.as_view(),
        name='room'),
]
