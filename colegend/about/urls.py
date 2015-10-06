from django.conf.urls import patterns, url
from about.views import IndexView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^about/2/$',
        IndexView.as_view(),
        name='index'),
)
