from django.conf.urls import patterns, url
from stats.views import StatsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        StatsView.as_view(),
        name='home'),
)
