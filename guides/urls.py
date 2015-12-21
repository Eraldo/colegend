from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from .views import GuideIntroductionView, GuideManageView, GuideDetailView, GuideListView, PersonalGuideView, \
    GuideesView, GuideActionView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='list', permanent=False),
        name='index'),
    url(r'^list$',
        GuideListView.as_view(),
        name='list'),
    url(r'^introduction$',
        GuideIntroductionView.as_view(),
        name='introduction'),
    url(r'^personal$',
        PersonalGuideView.as_view(),
        name='personal'),
    url(r'^guidees$',
        GuideesView.as_view(),
        name='guidees'),
    url(r'^(?P<owner>[\w.@+-]+)$',
        GuideDetailView.as_view(),
        name='detail'),
    url(r'^(?P<owner>[\w.@+-]+)/manage$',
        GuideManageView.as_view(),
        name='manage'),
    url(r'^(?P<owner>[\w.@+-]+)/guide$',
        GuideActionView.as_view(),
        name='guide-action'),
)
