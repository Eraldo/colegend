from django.conf.urls import patterns, url
from habits.views import HabitListView, HabitNewView, HabitShowView, HabitEditView, HabitDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        HabitListView.as_view(),
        name='habit_list'),

    # ex: ../new/
    url(r'^new/$',
        HabitNewView.as_view(),
        name='habit_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        HabitShowView.as_view(),
        name='habit_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        HabitEditView.as_view(),
        name='habit_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        HabitDeleteView.as_view(),
        name='habit_delete'),
)