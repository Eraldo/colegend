from django.conf.urls import url, include

from .views import JournalIndexView, JournalListView, JournalCreateView, JournalDetailView, JournalUpdateView, \
    JournalDeleteView, JournalDayView, JournalWeekView, JournalSettingsView, JournalSearchView, JournalMonthView

from .weekentries.urls import urlpatterns as week_urlpatterns
from .monthentries.urls import urlpatterns as month_urlpatterns

urlpatterns = [
    url(r'^$',
        JournalIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        JournalListView.as_view(),
        name='list'),
    url(r'^create/$',
        JournalCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        JournalDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        JournalUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        JournalDeleteView.as_view(),
        name='delete'),

    url(r'^(?P<pk>[0-9]+)/settings/$',
        JournalSettingsView.as_view(),
        name='settings'),
    url(r'^search/$',
        JournalSearchView.as_view(),
        name='search'),
    url(r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$',
        JournalDayView.as_view(),
        name='day'),
    url(r'^week/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$',
        JournalWeekView.as_view(),
        name='week'),
    url(r'^month/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$',
        JournalMonthView.as_view(),
        name='month'),
    # url(r'^week/(?P<year>[0-9]{4})-W(?P<week>[0-9]{2})/$',
    #     JournalWeekView.as_view(),
    #     name='week'),
]

urlpatterns = [
    url(r'^', include(urlpatterns, namespace='journals')),
    url(r'^weeks/', include(week_urlpatterns, namespace='weekentries')),
    url(r'^months/', include(month_urlpatterns, namespace='monthentries')),
]
