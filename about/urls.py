from django.conf.urls import patterns, url
from about.views import AboutView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        AboutView.as_view(),
        name='about'),
)
