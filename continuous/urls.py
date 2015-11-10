from django.conf.urls import patterns, url, include

from .views import ContinuousView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ContinuousView.as_view(),
        name='index'),
    url(r'^legend/', include('continuous.legend.urls', namespace='legend')),
)
