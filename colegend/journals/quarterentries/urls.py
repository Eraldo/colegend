from django.conf.urls import url

from .views import QuarterEntryIndexView, QuarterEntryListView, QuarterEntryCreateView, QuarterEntryDetailView, QuarterEntryUpdateView, \
    QuarterEntryDeleteView

urlpatterns = [
    url(r'^$',
        QuarterEntryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        QuarterEntryListView.as_view(),
        name='list'),
    url(r'^create/$',
        QuarterEntryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        QuarterEntryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        QuarterEntryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        QuarterEntryDeleteView.as_view(),
        name='delete'),
]
