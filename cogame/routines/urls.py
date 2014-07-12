from django.conf.urls import patterns, url
from routines.views import RoutineCheckView, RoutineDailyView, RoutineWeeklyView, RoutineMonthlyView, RoutineYearlyView, \
    RoutineListView, RoutineNewView, RoutineShowView, RoutineEditView, RoutineDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        RoutineListView.as_view(),
        name='routine_list'),

    # ex: ../new/
    url(r'^new/$',
        RoutineNewView.as_view(),
        name='routine_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        RoutineShowView.as_view(),
        name='routine_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        RoutineEditView.as_view(),
        name='routine_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        RoutineDeleteView.as_view(),
        name='routine_delete'),


    ## special routines

    # ex: ../check/
    url(r'^check$',
        RoutineCheckView.as_view(),
        name='routine_check'),

    # ex: ../daily/
    url(r'^daily$',
        RoutineDailyView.as_view(),
        name='routine_daily'),

    # ex: ../weekly/
    url(r'^weekly$',
        RoutineWeeklyView.as_view(),
        name='routine_weekly'),

    # ex: ../monthly/
    url(r'^monthly$',
        RoutineMonthlyView.as_view(),
        name='routine_monthly'),

    # ex: ../yearly/
    url(r'^yearly$',
        RoutineYearlyView.as_view(),
        name='routine_yearly'),
)
