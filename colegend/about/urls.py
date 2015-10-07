from django.conf.urls import patterns, url
from about.views import IndexView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^about/$',
        IndexView.as_view(),
        name='about'),
)
