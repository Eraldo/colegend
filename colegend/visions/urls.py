from django.conf.urls import url, include

from .views import VisionIndexView, VisionListView, VisionCreateView, VisionDetailView, VisionUpdateView, \
    VisionDeleteView

app_name = 'visions'
urlpatterns = [
    url(r'^$',
        VisionIndexView.as_view(),
        name='index'),
    url(r'^list/$',
        VisionListView.as_view(),
        name='list'),
    url(r'^(?P<scope>\w+)/', include([
        url(r'^create/$',
            VisionCreateView.as_view(),
            name='create'),
        url(r'^$',
            VisionDetailView.as_view(),
            name='detail'),
        url(r'^update/$',
            VisionUpdateView.as_view(),
            name='update'),
        url(r'^delete/$',
            VisionDeleteView.as_view(),
            name='delete'),
    ])),
]
