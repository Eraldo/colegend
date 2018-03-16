from django.conf.urls import url, include

from .views import ManagerIndexView

app_name = 'manager'
urlpatterns = [
    url(r'^$',
        ManagerIndexView.as_view(),
        name='index'),
]
