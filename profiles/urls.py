from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import BiographyUpdateView

__author__ = 'Eraldo Energy'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='biography/', permanent=False),
        name='index'),
    url(r'^biography/$',
        BiographyUpdateView.as_view(),
        name='biography'),
)
