# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView
from home.views import TestView, HomeView, JoinView

__author__ = 'Eraldo Energy'

BACKEND_NAME = 'coLegend backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = patterns(
    '',
    # Favicon
    url(r'^favicon\.ico$',
        RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # User management
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^join/$', JoinView.as_view(), name='join'),
    url(r'^legends/', include('legends.urls', namespace='legends')),
    url(r'^roles/', include('roles.urls', namespace='roles')),

    # Your stuff: custom urls includes go here
    url(r'^$', RedirectView.as_view(url='home/', permanent=False), name='index'),

    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^about/', include('about.urls')),
    url(r'^support/', include('support.urls', namespace='support')),

    url(r'^conscious/', include('conscious.urls', namespace='conscious')),
    url(r'^outer-call/', include('outercall.urls', namespace='outer-call')),
    url(r'^inner-call/', include('innercall.urls', namespace='inner-call')),

    url(r'^connected/', include('connected.urls', namespace='connected')),
    url(r'^guides/', include('guides.urls', namespace='guides')),

    url(r'^continuous/', include('continuous.urls', namespace='continuous')),
    url(r'^game/', include('game.urls', namespace='game')),
    url(r'^story/', include('story.urls', namespace='story')),

    url(r'^test/$', TestView.as_view(), name='test'),

    # Added robots.txt file for crawlers (google/etc)
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
