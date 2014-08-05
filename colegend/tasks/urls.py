from django.conf.urls import patterns, url
from tasks.views import TaskListView, TaskNewView, TaskShowView, TaskEditView, TaskDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        TaskListView.as_view(),
        name='task_list'),

    # ex: ../new/
    url(r'^new/$',
        TaskNewView.as_view(),
        name='task_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        TaskShowView.as_view(),
        name='task_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        TaskEditView.as_view(),
        name='task_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        TaskDeleteView.as_view(),
        name='task_delete'),
)