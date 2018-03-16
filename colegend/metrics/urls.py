from django.conf.urls import url

from .views import MetricsIndexView

app_name = 'metrics'
urlpatterns = [
    url(r'^$',
        MetricsIndexView.as_view(),
        name='index'),
]
