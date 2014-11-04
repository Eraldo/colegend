from django.conf.urls import patterns, url
from gatherings.views import GatheringsView, GatheringCreateView, GatheringEditView, GatheringDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        GatheringsView.as_view(),
        name='gatherings'),
    # ex: ../new/
    url(r'^new/$',
        GatheringCreateView.as_view(),
        name='gathering_new'),
    # ex: ../edit/
    url(r'^(?P<pk>\d+)/edit/$',
        GatheringEditView.as_view(),
        name='gathering_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        GatheringDeleteView.as_view(),
        name='gathering_delete'),

)
