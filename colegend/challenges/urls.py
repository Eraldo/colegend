from django.conf.urls import patterns, url
from challenges.views import ChallengeListView, ChallengeCreateView, ChallengeShowView, ChallengeEditView, \
    ChallengeDeleteView, HomeView, ModuleShowView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^home$',
        HomeView.as_view(),
        name='home'),
    # ex: ../module/4/
    url(r'^module/(?P<pk>\d+)/$',
        ModuleShowView.as_view(),
        name='module_show'),
    url(r'^$',
        ChallengeListView.as_view(),
        name='challenge_list'),
    # ex: ../new/
    url(r'^new/$',
        ChallengeCreateView.as_view(),
        name='challenge_new'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        ChallengeShowView.as_view(),
        name='challenge_show'),
    # ex: ../edit/
    url(r'^(?P<pk>\d+)/edit/$',
        ChallengeEditView.as_view(),
        name='challenge_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        ChallengeDeleteView.as_view(),
        name='challenge_delete'),

)
