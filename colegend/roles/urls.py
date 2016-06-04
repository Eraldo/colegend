from django.conf.urls import url, include

from .views import RoleIndexView, RoleListView, RoleCreateView, RoleDetailView, RoleUpdateView, \
    RoleDeleteView


urlpatterns = [
    url(r'^$',
        RoleIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        RoleListView.as_view(),
        name='list'),
    url(r'^create/$',
        RoleCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        RoleDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        RoleUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        RoleDeleteView.as_view(),
        name='delete'),
]
urlpatterns = [
    url(r'^', include(urlpatterns, namespace='roles')),
]
