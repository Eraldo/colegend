from django.conf.urls import url

from .views import YearEntryIndexView, YearEntryListView, YearEntryCreateView, YearEntryDetailView, YearEntryUpdateView, \
    YearEntryDeleteView

urlpatterns = [
    url(r'^$',
        YearEntryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        YearEntryListView.as_view(),
        name='list'),
    url(r'^create/$',
        YearEntryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        YearEntryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        YearEntryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        YearEntryDeleteView.as_view(),
        name='delete'),
]
