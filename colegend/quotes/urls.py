from django.conf.urls import patterns, url
from quotes.views import RandomQuoteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        RandomQuoteView.as_view(),
        name='random'),
)
