from django.conf.urls import url
from about.views import AboutView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        AboutView.as_view(),
        name='about'),
]
