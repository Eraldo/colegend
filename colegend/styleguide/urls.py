from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import StyleguideView

app_name = 'styleguide'
urlpatterns = [
    url(_(r'^$'), StyleguideView.as_view(), name='index'),
    url(_(r'^demos/(?P<template>.*)/$'), StyleguideView.as_view(), name='index'),
]
