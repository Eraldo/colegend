from django.conf.urls import url

from .views import CategoryIndexView, CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, \
    CategoryDeleteView

app_name = 'categories'
urlpatterns = [
    url(r'^$',
        CategoryIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        CategoryListView.as_view(),
        name='list'),
    url(r'^create/$',
        CategoryCreateView.as_view(),
        name='create'),
    url(r'^(?P<pk>[0-9]+)/$',
        CategoryDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        CategoryUpdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        CategoryDeleteView.as_view(),
        name='delete'),
]
