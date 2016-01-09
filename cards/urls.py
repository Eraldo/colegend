from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from .views import CardListView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='list/', permanent=False),
        name='index'),
    url(r'^list/$',
        CardListView.as_view(),
        name='list'),
)

card_urls = urlpatterns
