from django.conf.urls import url
from .views import DocumentationView, FAQView, SupportView

__author__ = 'eraldo'

urlpatterns = [
    url(r'^$',
        SupportView.as_view(),
        name='index'),
    url(r'^faq/$',
        FAQView.as_view(),
        name='faq'),
    url(r'^documentation/$',
        DocumentationView.as_view(),
        name='documentation'),
]
