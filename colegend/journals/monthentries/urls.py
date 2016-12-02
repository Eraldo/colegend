from django.conf.urls import url

from .views import MonthEntryIndexView, MonthEntryListView, MonthEntryCreateView, MonthEntryDetailView, MonthEntryUpdateView, \
    MonthEntryDeleteView

urlpatterns = [
    url(r'^$',
        MonthEntryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        MonthEntryListView.as_view(),
        name='list'),
    url(r'^create/$',
        MonthEntryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        MonthEntryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        MonthEntryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        MonthEntryDeleteView.as_view(),
        name='delete'),
]
