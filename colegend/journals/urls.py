from django.conf.urls import patterns, url
from journals.views import DayEntryShowView, DayEntryNewView, DayEntryEditView, DayEntryDeleteView, DayEntryListView, \
    DayEntryContinueView, MapView, JournalEditView, EntryChartView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../4/edit/
    url(r'^edit/$',
        JournalEditView.as_view(),
        name='journal_edit'),

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

    # ex: ../1985-01-07/
    url(r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$',
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

    # ex: ../map/
    url(r'^map/$',
        MapView.as_view(),
        name='map'),

    # ex: ../chart/
    url(r'^chart/$',
        EntryChartView.as_view(),
        name='entry_chart'),
)
