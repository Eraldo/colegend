from django.conf.urls import patterns, url
from trackers.views import TrackerListView, WeightListView, WeightNewView, WeightEditView, WeightDeleteView, \
    WeightShowView, SexListView, SexNewView, SexShowView, SexEditView, SexDeleteView, BookListView, BookNewView, \
    BookShowView, BookEditView, BookDeleteView, JokeListView, JokeNewView, JokeShowView, JokeEditView, JokeDeleteView, \
    TransactionListView, TransactionNewView, TransactionShowView, TransactionEditView, TransactionDeleteView, \
    DreamListView, DreamNewView, DreamShowView, DreamEditView, DreamDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        TrackerListView.as_view(),
        name='tracker_list'),

    # ex: ../weight/
    url(r'^weight/$',
        WeightListView.as_view(),
        name='weight_list'),

    # ex: ../weight/new/
    url(r'^weight/new/$',
        WeightNewView.as_view(),
        name='weight_new'),

    # ex: ../weight/4/
    url(r'^weight/(?P<pk>\d+)/$',
        WeightShowView.as_view(),
        name='weight_show'),

    # ex: ../weight/4/edit/
    url(r'^weight/(?P<pk>\d+)/edit/$',
        WeightEditView.as_view(),
        name='weight_edit'),

    # ex: ..weight/4/delete/
    url(r'^weight/(?P<pk>\d+)/delete/$',
        WeightDeleteView.as_view(),
        name='weight_delete'),


    # ex: ../sex/
    url(r'^sex/$',
        SexListView.as_view(),
        name='sex_list'),

    # ex: ../sex/new/
    url(r'^sex/new/$',
        SexNewView.as_view(),
        name='sex_new'),

    # ex: ../sex/4/
    url(r'^sex/(?P<pk>\d+)/$',
        SexShowView.as_view(),
        name='sex_show'),

    # ex: ../sex/4/edit/
    url(r'^sex/(?P<pk>\d+)/edit/$',
        SexEditView.as_view(),
        name='sex_edit'),

    # ex: ..sex/4/delete/
    url(r'^sex/(?P<pk>\d+)/delete/$',
        SexDeleteView.as_view(),
        name='sex_delete'),


    # ex: ../book/
    url(r'^book/$',
        BookListView.as_view(),
        name='book_list'),

    # ex: ../book/new/
    url(r'^book/new/$',
        BookNewView.as_view(),
        name='book_new'),

    # ex: ../book/4/
    url(r'^book/(?P<pk>\d+)/$',
        BookShowView.as_view(),
        name='book_show'),

    # ex: ../book/4/edit/
    url(r'^book/(?P<pk>\d+)/edit/$',
        BookEditView.as_view(),
        name='book_edit'),

    # ex: ..book/4/delete/
    url(r'^book/(?P<pk>\d+)/delete/$',
        BookDeleteView.as_view(),
        name='book_delete'),


    # ex: ../joke/
    url(r'^joke/$',
        JokeListView.as_view(),
        name='joke_list'),

    # ex: ../joke/new/
    url(r'^joke/new/$',
        JokeNewView.as_view(),
        name='joke_new'),

    # ex: ../joke/4/
    url(r'^joke/(?P<pk>\d+)/$',
        JokeShowView.as_view(),
        name='joke_show'),

    # ex: ../joke/4/edit/
    url(r'^joke/(?P<pk>\d+)/edit/$',
        JokeEditView.as_view(),
        name='joke_edit'),

    # ex: ..joke/4/delete/
    url(r'^joke/(?P<pk>\d+)/delete/$',
        JokeDeleteView.as_view(),
        name='joke_delete'),


    # ex: ../transaction/
    url(r'^transaction/$',
        TransactionListView.as_view(),
        name='transaction_list'),

    # ex: ../transaction/new/
    url(r'^transaction/new/$',
        TransactionNewView.as_view(),
        name='transaction_new'),

    # ex: ../transaction/4/
    url(r'^transaction/(?P<pk>\d+)/$',
        TransactionShowView.as_view(),
        name='transaction_show'),

    # ex: ../transaction/4/edit/
    url(r'^transaction/(?P<pk>\d+)/edit/$',
        TransactionEditView.as_view(),
        name='transaction_edit'),

    # ex: ..transaction/4/delete/
    url(r'^transaction/(?P<pk>\d+)/delete/$',
        TransactionDeleteView.as_view(),
        name='transaction_delete'),


    # ex: ../dream/
    url(r'^dream/$',
        DreamListView.as_view(),
        name='dream_list'),

    # ex: ../dream/new/
    url(r'^dream/new/$',
        DreamNewView.as_view(),
        name='dream_new'),

    # ex: ../dream/4/
    url(r'^dream/(?P<pk>\d+)/$',
        DreamShowView.as_view(),
        name='dream_show'),

    # ex: ../dream/4/edit/
    url(r'^dream/(?P<pk>\d+)/edit/$',
        DreamEditView.as_view(),
        name='dream_edit'),

    # ex: ..dream/4/delete/
    url(r'^dream/(?P<pk>\d+)/delete/$',
        DreamDeleteView.as_view(),
        name='dream_delete'),
)
