from django.conf.urls import patterns, url
from .views import GameIndexView, CompletedView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        GameIndexView.as_view(),
        name='index'),
    url(r'^completed/$',
        CompletedView.as_view(),
        name='completed'),
)

card_urls = urlpatterns
