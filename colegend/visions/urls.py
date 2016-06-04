from django.conf.urls import url

from .views import VisionIndexView, VisionListView, VisionCreateView, VisionDetailView, VisionUpdateView, \
    VisionDeleteView


urlpatterns = [
    url(r'^$',
        VisionIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        VisionListView.as_view(),
        name='list'),
    url(r'^create/$',
        VisionCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        VisionDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        VisionUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        VisionDeleteView.as_view(),
        name='delete'),
]
