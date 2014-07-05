from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectNewView, ProjectShowView, ProjectEditView, ProjectDeleteView

__author__ = 'eraldo'


urlpatterns = patterns('',
    # ex: ../
    url(r'^$',
        ProjectListView.as_view(),
        name='project_list'),

    # ex: ../new/
    url(r'^new/$',
        ProjectNewView.as_view(),
        name='project_new'),

        # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        ProjectShowView.as_view(),
        name='project_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        ProjectEditView.as_view(),
        name='project_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        ProjectDeleteView.as_view(),
        name='project_delete'),
    )
