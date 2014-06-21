from django.conf.urls import patterns, url
from tags.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TagDetailView

__author__ = 'eraldo'


urlpatterns = patterns('',
 # ex: ../tags/
    url(r'^$',
        TagListView.as_view(),
        name='list'),

    # ex: ../create/
    url(r'^create/$',
        TagCreateView.as_view(),
        name='create'),

        # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        TagDetailView.as_view(),
        name='detail'),

    # ex: ../4/update/
    url(r'^(?P<pk>\d+)/update/$',
        TagUpdateView.as_view(),
        name='update'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        TagDeleteView.as_view(),
        name='delete'),
    )