from django.conf.urls import patterns, url
from projects.views import ProjectListView

__author__ = 'eraldo'


urlpatterns = patterns('',
 # ex: ../projects/
    url(r'^$',
        ProjectListView.as_view(),
        name='list'),
    )