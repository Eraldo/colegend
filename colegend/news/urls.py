from django.conf.urls import patterns, url
from news.views import NewsBlockListView, NewsBlockCreateView, NewsBlockShowView, NewsBlockEditView, NewsBlockDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        NewsBlockListView.as_view(),
        name='newsblock_list'),
    # ex: ../new/
    url(r'^new/$',
        NewsBlockCreateView.as_view(),
        name='newsblock_new'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        NewsBlockShowView.as_view(),
        name='newsblock_show'),
    # ex: ../edit/
    url(r'^(?P<pk>\d+)/edit/$',
        NewsBlockEditView.as_view(),
        name='newsblock_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        NewsBlockDeleteView.as_view(),
        name='newsblock_delete'),

)
