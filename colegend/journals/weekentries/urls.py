from django.conf.urls import url

from .views import WeekEntryIndexView, WeekEntryListView, WeekEntryCreateView, WeekEntryDetailView, WeekEntryUpdateView, \
    WeekEntryDeleteView

urlpatterns = [
    url(r'^$',
        WeekEntryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        WeekEntryListView.as_view(),
        name='list'),
    url(r'^create/$',
        WeekEntryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        WeekEntryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        WeekEntryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        WeekEntryDeleteView.as_view(),
        name='delete'),
]
