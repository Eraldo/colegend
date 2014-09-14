from django.conf.urls import patterns, url
from users.views import UserInactiveView, UserListView, UserRedirectView, UserDetailView, UserUpdateView, \
    SettingsUpdateView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # URL pattern for the UserListView
    url(
        regex=r'^inactive$',
        view=UserInactiveView.as_view(),
        name='inactive'
    ),
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
    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=UserDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=UserUpdateView.as_view(),
        name='update'
    ),

    # SETTINGS

    url(
        regex=r'^~settings/$',
        # regex=r'^settings/(?P<owner>[\w.@+-]+)/$',
        view=SettingsUpdateView.as_view(),
        name='settings'
    ),


)
