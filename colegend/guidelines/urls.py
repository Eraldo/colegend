from django.conf.urls import url, include
from .views import GuidelinesView, GuidelinesIntroductionView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        GuidelinesView.as_view(),
        name='index'),
    url(r'^introduction/$',
        GuidelinesIntroductionView.as_view(),
        name='introduction'),
]
urlpatterns = [
    url(r'^', include(urlpatterns, namespace='guidelines')),
]
