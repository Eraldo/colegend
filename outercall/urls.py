from django.conf.urls import patterns, url
from .views import OuterCallCreateView, OuterCallUpdateView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        OuterCallCreateView.as_view(),
        name='create'),
    url(r'^update$',
        OuterCallUpdateView.as_view(),
        name='update'),
)
