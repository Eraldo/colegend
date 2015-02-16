from django.conf.urls import patterns, url
from cards.views import CardPickerView, CardShowView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        CardPickerView.as_view(),
        name='picker'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        CardShowView.as_view(),
        name='card_show'),
)
