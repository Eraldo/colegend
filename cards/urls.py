from django.conf.urls import url
from django.views.generic import RedirectView

from .views import CardListView, CardDetailView, CardUpdateView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(url='list/', permanent=False),
        name='index'),
    url(r'^list/$',
        CardListView.as_view(),
        name='list'),
    url(r'^(?P<pk>[0-9]+)/$',
        CardDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        CardUpdateView.as_view(),
        name='update'),
]

card_urls = urlpatterns
