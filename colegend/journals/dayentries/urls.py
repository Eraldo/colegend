from django.conf.urls import url

from .views import DayEntryIndexView, DayEntryListView, DayEntryCreateView, DayEntryDetailView, DayEntryUpdateView, \
    DayEntryDeleteView

urlpatterns = [
    url(r'^$',
        DayEntryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        DayEntryListView.as_view(),
        name='list'),
    url(r'^create/$',
        DayEntryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        DayEntryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        DayEntryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        DayEntryDeleteView.as_view(),
        name='delete'),
]
