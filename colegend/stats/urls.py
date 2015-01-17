from django.conf.urls import patterns, url
from stats.views import StatsView, AdminStatsView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        StatsView.as_view(),
        name='home'),
    # ex: ../admin/
    url(r'^admin$',
        AdminStatsView.as_view(),
        name='admin'),
)
