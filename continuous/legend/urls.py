from django.conf.urls import patterns, url

from .views import Chapter1View

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^chapter-1$',
        Chapter1View.as_view(),
        name='chapter1'),
)
