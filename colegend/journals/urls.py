from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from journals.views import DayEntryShowView, DayEntryNewView, DayEntryEditView, DayEntryDeleteView, DayEntryListView, \
    DayEntryContinueView, MapView, JournalEditView, WeekView, WeekEntryNewView, WeekEntryShowView, \
    WeekEntryEditView, WeekEntryDeleteView, DayEntryChartView, WeekEntryChartView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        RedirectView.as_view(url='./week'),
        name='index'),

    # ex: ../4/edit/
    url(r'^edit/$',
        JournalEditView.as_view(),
        name='journal_edit'),

    # ex: ../list/
    url(r'^list$',
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


    # ex: ../week/1985-01-07/
    url(r'^week/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$',
        WeekView.as_view(),
        name='week'),

    # ex: ../week/
    url(r'^week/$',
        WeekView.as_view(),
        name='week'),


    # ex: ../week/1985-01-07/show/
    url(r'^week/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/show/$',
        WeekEntryShowView.as_view(),
        name='weekentry_show'),

    # ex: ../week/new/
    url(r'^week/new/$',
        WeekEntryNewView.as_view(),
        name='weekentry_new'),

    # ex: ../week/1985-01-07/edit/
    url(r'^week/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/edit/$',
        WeekEntryEditView.as_view(),
        name='weekentry_edit'),

    # ex: ../week/1985-01-07/delete/
    url(r'^week/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/delete/$',
        WeekEntryDeleteView.as_view(),
        name='weekentry_delete'),

    # ex: ../map/
    url(r'^map/$',
        MapView.as_view(),
        name='map'),

    # ex: ../day/chart/
    url(r'^day/chart/$',
        DayEntryChartView.as_view(),
        name='dayentry_chart'),

    # ex: ../week/chart/
    url(r'^week/chart/$',
        WeekEntryChartView.as_view(),
        name='weekentry_chart'),
)
