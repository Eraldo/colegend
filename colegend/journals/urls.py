from django.conf.urls import patterns, url
from journals.views import DayEntryShowView, DayEntryNewView, DayEntryEditView, DayEntryDeleteView, DayEntryListView, \
    DayEntryContinueView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        DayEntryListView.as_view(),
        name='dayentry_list'),

    # ex: ../new/
    url(r'^new/$',
        DayEntryNewView.as_view(),
        name='dayentry_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        DayEntryShowView.as_view(),
        name='dayentry_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        DayEntryEditView.as_view(),
        name='dayentry_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        DayEntryDeleteView.as_view(),
        name='dayentry_delete'),

    # ex: ../continue/
    url(r'^continue/$',
        DayEntryContinueView.as_view(),
        name='dayentry_continue'),
)
