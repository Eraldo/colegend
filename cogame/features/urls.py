from django.conf.urls import patterns, url
from features.views import FeatureListView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        FeatureListView.as_view(),
        name='feature_list'),

)