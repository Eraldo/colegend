from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectDetailView

__author__ = 'eraldo'


urlpatterns = patterns('',
 # ex: ../projects/
    url(r'^$',
        ProjectListView.as_view(),
        name='list'),

    # ex: ../create/
    url(r'^create/$',
        ProjectCreateView.as_view(),
        name='create'),

        # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        ProjectDetailView.as_view(),
        name='detail'),

    # ex: ../4/update/
    url(r'^(?P<pk>\d+)/update/$',
        ProjectUpdateView.as_view(),
        name='update'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        ProjectDeleteView.as_view(),
        name='delete'),
    )