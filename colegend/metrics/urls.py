from django.conf.urls import url

from .views import MetricsIndexView

urlpatterns = [
    url(r'^$',
        MetricsIndexView.as_view(),
        name='index'),
]
