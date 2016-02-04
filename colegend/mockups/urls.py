from django.conf.urls import url

from .views import MockupView

urlpatterns = [
    url(r'^(?P<template>.*)/$',
        MockupView.as_view(),
        name='mockup'),
]
