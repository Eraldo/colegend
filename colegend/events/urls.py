from django.conf.urls import url, include

from .views import EventIndexView, EventCalendarView

urlpatterns = [
    url(r'^$',
        EventIndexView.as_view(),
        name='index'),
    url(r'^calendar/$',
        EventCalendarView.as_view(),
        name='calendar'),
]

urlpatterns = [
    url(r'^', include(urlpatterns, namespace='events')),
]
