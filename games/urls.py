from django.conf.urls import patterns, url
from .views import GameIndexView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        GameIndexView.as_view(),
        name='index'),
)

card_urls = urlpatterns
