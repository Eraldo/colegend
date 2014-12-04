from django.conf.urls import patterns, url
from manager.views import AgendaView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        AgendaView.as_view(),
        name='agenda'),
)
