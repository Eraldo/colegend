from django.conf.urls import url

from .views import TagIndexView, TagListView, TagCreateView, TagDetailView, TagUpdateView, \
    TagDeleteView

urlpatterns = [
    url(r'^$',
        TagIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        TagListView.as_view(),
        name='list'),
    url(r'^create/$',
        TagCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        TagDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        TagUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        TagDeleteView.as_view(),
        name='delete'),
]
