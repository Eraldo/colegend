from django.conf.urls import patterns, url
from .views import InnerCallCreateView, InnerCallUpdateView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        InnerCallCreateView.as_view(),
        name='create'),
    url(r'^update$',
        InnerCallUpdateView.as_view(),
        name='update'),
)
