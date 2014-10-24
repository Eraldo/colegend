from django.conf.urls import patterns, url
from challenges.views import ChallengeListView, ChallengeCreateView, ChallengeShowView, ChallengeEditView, \
    ChallengeDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
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
