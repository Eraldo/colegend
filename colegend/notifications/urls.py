from django.conf.urls import patterns, url
from notifications.views import NotificationListView, NotificationNewView, NotificationShowView, NotificationEditView, NotificationDeleteView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    # ex: ../
    url(r'^$',
        NotificationListView.as_view(),
        name='notification_list'),

    # ex: ../new/
    url(r'^new/$',
        NotificationNewView.as_view(),
        name='notification_new'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        NotificationShowView.as_view(),
        name='notification_show'),

    # ex: ../4/edit/
    url(r'^(?P<pk>\d+)/edit/$',
        NotificationEditView.as_view(),
        name='notification_edit'),

    # ex: ../4/delete/
    url(r'^(?P<pk>\d+)/delete/$',
        NotificationDeleteView.as_view(),
        name='notification_delete'),
)
