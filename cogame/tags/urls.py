from django.conf.urls import patterns, url
from tags.views import TagListView, TagNewView, TagShowView, TagEditView, TagDeleteView

__author__ = 'eraldo'


urlpatterns = patterns('',
 # ex: ../
    url(r'^$',
        TagListView.as_view(),
        name='tag_list'),

    # ex: ../new/
    url(r'^new/$',
        TagNewView.as_view(),
        name='tag_new'),

        # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        TagShowView.as_view(),
        name='tag_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        TagEditView.as_view(),
        name='tag_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        TagDeleteView.as_view(),
        name='tag_delete'),
    )