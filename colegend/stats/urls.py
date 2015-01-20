from django.conf.urls import patterns, url
from stats.views import StatsView, ManagerStatsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        StatsView.as_view(),
        name='home'),
    # ex: ../admin/
    url(r'^manager$',
        ManagerStatsView.as_view(),
        name='manager'),
)
