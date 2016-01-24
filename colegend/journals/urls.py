from django.conf.urls import url, include

from .views import JournalIndexView, JournalListView, JournalCreateView, JournalDetailView, JournalUpdateView, \
    JournalDeleteView

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
]
