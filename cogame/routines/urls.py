from django.conf.urls import patterns, url
from routines.views import RoutineCheckView, RoutineDailyView, RoutineWeeklyView, RoutineMonthlyView, RoutineYearlyView

__author__ = 'eraldo'


urlpatterns = patterns('',
    url(r'^$',
        RoutineCheckView.as_view(),
        name='routine_check'),

    url(r'^daily$',
        RoutineDailyView.as_view(),
        name='routine_daily'),

    url(r'^weekly$',
        RoutineWeeklyView.as_view(),
        name='routine_weekly'),

    url(r'^monthly$',
        RoutineMonthlyView.as_view(),
        name='routine_monthly'),

    url(r'^yearly$',
        RoutineYearlyView.as_view(),
        name='routine_yearly'),
)
