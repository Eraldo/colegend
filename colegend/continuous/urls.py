from django.conf.urls import url
from .views import ContinuousView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        ContinuousView.as_view(),
        name='index'),
]
