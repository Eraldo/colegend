from django.conf.urls import patterns, url
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

__author__ = 'eraldo'


urlpatterns = patterns('',
 # ex: ../tasks/
    url(r'^$',
        TaskListView.as_view(),
        name='list'),

    # ex: ../create/
    url(r'^create/$',
        TaskCreateView.as_view(),
        name='create'),

        # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        TaskDetailView.as_view(),
        name='detail'),

    # ex: ../4/update/
    url(r'^(?P<pk>\d+)/update/$',
        TaskUpdateView.as_view(),
        name='update'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        TaskDeleteView.as_view(),
        name='delete'),
    )