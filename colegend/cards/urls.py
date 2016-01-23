from django.conf.urls import url
from django.views.generic import RedirectView

from .views import CardListView, CardDetailView, CardUpdateView, CardDeleteView, CardCreateView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(url='list/', permanent=False),
        name='index'),
    url(r'^list/$',
        CardListView.as_view(),
        name='list'),
    url(r'^create/$',
        CardCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        CardDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        CardUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        CardDeleteView.as_view(),
        name='delete'),
]

card_urls = urlpatterns
