# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from .views import UserListView, UserRedirectView, SettingsView, ProfileView, UserUpdateView

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the SettingsView
    url(
        regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='settings'
    ),

    # URL pattern for the ProfileView
    url(
        regex=r'^profile/(?P<username>[\w.@+-]+)/$',
        view=ProfileView.as_view(),
        name='profile'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=UserUpdateView.as_view(),
        name='update'
    ),
]
