from django.conf.urls import patterns, url
from visions.views import VisionListView, VisionNewView, VisionShowView, VisionEditView, VisionDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        VisionListView.as_view(),
        name='vision_list'),

    # ex: ../new/
    url(r'^new/$',
        VisionNewView.as_view(),
        name='vision_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        VisionShowView.as_view(),
        name='vision_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        VisionEditView.as_view(),
        name='vision_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        VisionDeleteView.as_view(),
        name='vision_delete'),
)
