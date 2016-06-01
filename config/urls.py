# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView

from colegend.home.views import JoinView

__author__ = 'Eraldo Energy'

BACKEND_NAME = 'coLegend backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = [
    # Favicon
    url(r'^favicon\.ico$',
        RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'), permanent=True)),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

    # User management
    url(r'^legends/', include('colegend.users.urls', namespace='legends')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^join/$', JoinView.as_view(), name='join'),
    url(r'^roles/', include('colegend.roles.urls', namespace='roles')),
    url(r'^tags/', include('colegend.tags.urls', namespace='tags')),
    url(r'^category/', include('colegend.categories.urls', namespace='categories')),
    url(r'^donations/', include('colegend.donations.urls', namespace='donations')),

    # Your stuff: custom urls includes go here
    url(r'^days/', include('colegend.dayentries.urls', namespace='dayentries')),

    url(r'^outer-call/', include('colegend.outercall.urls', namespace='outer-call')),
    url(r'^inner-call/', include('colegend.innercall.urls', namespace='inner-call')),
    url(r'^biography/', include('colegend.biography.urls', namespace='biography')),

    url(r'^cards/', include('colegend.cards.urls', namespace='cards')),

    # Added robots.txt file for crawlers (google/etc)
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    url(r'^mockups/', include('colegend.mockups.urls')),
    url(r'^styleguide/', include('colegend.styleguide.urls')),

]
# Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.

    # error pages
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

    import debug_toolbar

    # debug-toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    # CMS
    url(r'^files/', include('filer.urls')),
    url(r'^', include('cms.urls')),
]
