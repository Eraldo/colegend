from django.conf.urls import url
from .views import ConsciousView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        ConsciousView.as_view(),
        name='index'),
]
