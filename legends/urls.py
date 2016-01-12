from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import LegendDetailView, LegendListView, LegendUpdateView, BiographyUpdateView, \
    LegendAvatarView

__author__ = 'Eraldo Energy'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='legend/', permanent=False),
        name='index'),
    url(r'^list/$',
        LegendListView.as_view(),
        name='list'),
    url(r'^legend/$',
        LegendDetailView.as_view(),
        name='legend'),
    url(r'^biography/$',
        BiographyUpdateView.as_view(),
        name='biography'),
    url(r'^(?P<owner>[\w.@+-]+)/$',
        LegendDetailView.as_view(),
        name='detail'),
    url(r'^(?P<owner>[\w.@+-]+)/update/$',
        LegendUpdateView.as_view(),
        name='update'),
    url(r'^(?P<owner>[\w.@+-]+)/update/avatar/$',
        LegendAvatarView.as_view(),
        name='avatar'),
)
