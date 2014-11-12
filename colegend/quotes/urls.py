from django.conf.urls import patterns, url
from quotes.views import QuoteCreateView, QuoteListView, QuoteShowView, QuoteEditView, QuoteDeleteView, \
    QuoteManageView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        QuoteListView.as_view(),
        name='quote_list'),
    # ex: ../new/
    url(r'^new/$',
        QuoteCreateView.as_view(),
        name='quote_new'),
    # ex: ../manage/
    url(r'^manage/$',
        QuoteManageView.as_view(),
        name='quote_manage'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        QuoteShowView.as_view(),
        name='quote_show'),
    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        QuoteEditView.as_view(),
        name='quote_edit'),
    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        QuoteDeleteView.as_view(),
        name='quote_delete'),
)
