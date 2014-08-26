from django.conf.urls import patterns, url
from contact.views import ContactView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        ContactView.as_view(),
        name='contact'),
)
