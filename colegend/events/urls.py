from django.conf.urls import url

from .views import EventIndexView, EventCalendarView

urlpatterns = [
    url(r'^$',
        EventIndexView.as_view(),
        name='index'),
    url(r'^calendar/$',
        EventCalendarView.as_view(),
        name='calendar'),
]
