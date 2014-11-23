from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from tutorials.models import Tutorial
from tutorials.views import TutorialListView, TutorialCreateView, TutorialShowView, TutorialEditView, \
    TutorialDeleteView, TutorialRedirectView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        TutorialListView.as_view(),
        name='tutorial_list'),
    # ex: ../new/
    url(r'^new/$',
        TutorialCreateView.as_view(),
        name='tutorial_new'),
    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        TutorialShowView.as_view(),
        name='tutorial_show'),
    # ex: ../edit/
    url(r'^(?P<pk>\d+)/edit/$',
        TutorialEditView.as_view(),
        name='tutorial_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        TutorialDeleteView.as_view(),
        name='tutorial_delete'),

    # ex: ../text-areas
    url(r'^text-areas/$',
        TutorialRedirectView.as_view(),
        name='text-areas'),
)
