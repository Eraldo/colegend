# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import RedirectView

from colegend.views import TestView, HomeView

__author__ = 'Eraldo Energy'


BACKEND_NAME = 'coLegend backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

print(settings.ADMIN_URL)
urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # User management
    url(r'^users/', include('colegend.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/', include('about.urls')),
    url(r'^conscious/', include('conscious.urls', namespace='conscious')),
    url(r'^connected/', include('connected.urls', namespace='connected')),
    url(r'^continuous/', include('continuous.urls', namespace='continuous')),
    url(r'^test/$', TestView.as_view(), name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
