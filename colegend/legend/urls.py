from django.conf.urls import patterns, url
from legend.views import LegendView
from tags.views import TagListView, TagNewView, TagShowView, TagEditView, TagDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        LegendView.as_view(),
        name='home'),
)
