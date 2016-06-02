from django.conf.urls import url, include
from .views import GameIndexView, CompletedView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        GameIndexView.as_view(),
        name='index'),
    url(r'^completed/$',
        CompletedView.as_view(),
        name='completed'),
]
urlpatterns = [
    url(r'^', include(urlpatterns, namespace='games')),
]
