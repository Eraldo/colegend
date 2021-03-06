# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from wagtail.search import urls as wagtailsearch_urls

from colegend.about.views import AcademyView

__author__ = 'Eraldo Energy'

BACKEND_NAME = 'coLegend backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = [
    # Favicon
    url(r'^favicon\.ico$',
        RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'), permanent=True)),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^{}/'.format(settings.ADMIN_URL), admin.site.urls),

    # User management
    url(r'^accounts/', include('allauth.urls')),

    url(r'^legends/', include('colegend.users.urls')),
    url(r'^outer-call/', include('colegend.outercall.urls')),
    url(r'^inner-call/', include('colegend.innercall.urls')),
    url(r'^biography/', include('colegend.biography.urls')),

    url(r'^tags/', include('colegend.tags.urls')),

    # Your stuff: custom urls includes go here
    # url(r'^$', RedirectView.as_view(url='home/', permanent=False), name='index'),

    url(r'^donations/', include('colegend.donations.urls')),
    url(r'^roles/', include('colegend.roles.urls')),
    url(r'^category/', include('colegend.categories.urls')),

    url(r'^manager/', include('colegend.manager.urls')),
    url(r'^outcomes/', include('colegend.outcomes.urls')),
    url(r'^vision/', include('colegend.visions.urls')),
    url(r'^journal/', include('colegend.journals.urls')),

    # url(r'^guides/', include('colegend.guides.urls')),
    # url(r'^chat/', include('colegend.chat.urls')),
    url(r'^guidelines/', include('colegend.guidelines.urls')),

    # url(r'^tutorial/', include('colegend.games.urls')),
    # url(r'^cards/', include('colegend.cards.urls', namespace='cards')),
    # url(r'^story/', include('colegend.story.urls')),

    # Added robots.txt file for crawlers (google/etc)
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    url(r'^styleguide/', include('colegend.styleguide.urls')),
    # url(r'^sandbox/', include('colegend.sandbox.urls')),
    # url(r'^mockups/', include('colegend.mockups.urls')),
    url(r'^metrics/', include('colegend.metrics.urls')),

    # API
    url(r'^api/', include('colegend.api.urls')),

    # temp content
    url(r'^academy/', AcademyView.as_view()),
    url(r'^coacademy/', AcademyView.as_view()),
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
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^', include(wagtail_urls)),
]
