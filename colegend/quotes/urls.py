from django.conf.urls import patterns, url
from quotes.views import RandomQuoteView, QuoteCreateView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        RandomQuoteView.as_view(),
        name='random'),
    # ex: ../new/
    url(r'^new/$',
        QuoteCreateView.as_view(),
        name='quote_new'),
)
