# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView

from colegend.home.views import TestView, HomeView, JoinView

__author__ = 'Eraldo Energy'

BACKEND_NAME = 'coLegend backend'
admin.site.site_header = BACKEND_NAME
admin.site.site_title = BACKEND_NAME

urlpatterns = [
                  # Favicon
                  url(r'^favicon\.ico$',
                      RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),

                  # Django Admin, use {% url 'admin:index' %}
                  url(r'^{}/'.format(settings.ADMIN_URL), include(admin.site.urls)),

                  # User management
                  url(r'^legends/', include('colegend.users.urls', namespace='legends')),
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^join/$', JoinView.as_view(), name='join'),
                  url(r'^roles/', include('colegend.roles.urls', namespace='roles')),
                  url(r'^tags/', include('colegend.tags.urls', namespace='tags')),

                  # Your stuff: custom urls includes go here
                  url(r'^$', RedirectView.as_view(url='home/', permanent=False), name='index'),

                  url(r'^home/$', HomeView.as_view(), name='home'),
                  url(r'^about/', include('colegend.about.urls')),
                  url(r'^support/', include('colegend.support.urls', namespace='support')),

                  url(r'^conscious/', include('colegend.conscious.urls', namespace='conscious')),
                  url(r'^journals/', include('colegend.journals.urls', namespace='journals')),
                  url(r'^dayentries/', include('colegend.dayentries.urls', namespace='dayentries')),

                  url(r'^connected/', include('colegend.connected.urls', namespace='connected')),
                  url(r'^outer-call/', include('colegend.outercall.urls', namespace='outer-call')),
                  url(r'^inner-call/', include('colegend.innercall.urls', namespace='inner-call')),
                  url(r'^biography/', include('colegend.biography.urls', namespace='biography')),
                  url(r'^guides/', include('colegend.guides.urls', namespace='guides')),

                  url(r'^continuous/', include('colegend.continuous.urls', namespace='continuous')),
                  url(r'^games/', include('colegend.games.urls', namespace='games')),
                  url(r'^cards/', include('colegend.cards.urls', namespace='cards')),
                  url(r'^story/', include('colegend.story.urls', namespace='story')),

                  url(r'^test/$', TestView.as_view(), name='test'),

                  # Added robots.txt file for crawlers (google/etc)
                  url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

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
