from django.conf.urls import url

from .views import OutcomeIndexView, OutcomeListView, OutcomeCreateView, OutcomeDetailView, OutcomeUpdateView, \
    OutcomeDeleteView, OutcomeInboxView, OutcomeAutocompleteView

urlpatterns = [
    url(r'^$',
        OutcomeIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        OutcomeListView.as_view(),
        name='list'),
    url(r'^inbox/$',
        OutcomeInboxView.as_view(),
        name='inbox'),
    url(r'^create/$',
        OutcomeCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        OutcomeDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        OutcomeUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        OutcomeDeleteView.as_view(),
        name='delete'),

    url(
        'autocomplete/$',
        OutcomeAutocompleteView.as_view(),
        name='autocomplete',
    ),
]
