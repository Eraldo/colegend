from django.conf.urls import url, include

from .views import ManagerIndexView

urlpatterns = [
    url(r'^$',
        ManagerIndexView.as_view(),
        name='index'),
]
