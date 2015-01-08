from django.conf.urls import patterns, url
from users.views import UserInactiveView, UserListView, UserRedirectView, UserDetailView, UserUpdateView, \
    SettingsUpdateView, UserManageListView, UserManageDetailView, UserAdminDetailView, MapView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',

    # OTHER

    # ex: ../map/
    url(
        regex=r'^map/$',
        view=MapView.as_view(),
        name='map'
    ),

    # MAIN

    # URL pattern for the UserListView
    url(
        regex=r'^inactive$',
        view=UserInactiveView.as_view(),
        name='inactive'
    ),
    url(
        regex=r'^manage$',
        view=UserManageListView.as_view(),
        name='manage'
    ),
    url(
        regex=r'^manage/(?P<username>[\w.@+-]+)/$',
        view=UserManageDetailView.as_view(),
        name='manage_detail'
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
        view=SettingsUpdateView.as_view(),
        name='settings'
    ),

    # ADMIN

    url(
        regex=r'^(?P<username>[\w.@+-]+)/admin/$',
        view=UserAdminDetailView.as_view(),
        name='admin_detail'
    ),

)
