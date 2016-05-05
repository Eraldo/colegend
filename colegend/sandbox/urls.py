from django.conf.urls import url

from .views import SandboxView

urlpatterns = [
    url(r'^$',
        SandboxView.as_view(),
        name='sandbox'),
]
