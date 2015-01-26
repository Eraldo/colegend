from django.conf.urls import patterns, url
from contact.views import ContactView, MessageView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        ContactView.as_view(),
        name='contact'),

    url(r'^message/$',
        MessageView.as_view(),
        name='message'),
)
