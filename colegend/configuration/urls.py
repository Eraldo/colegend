from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'configuration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # main urls
    url(r'', include('website.urls')),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^tasks/', include('tasks.urls', namespace="tasks")),
    url(r'^routines/', include('routines.urls', namespace="routines")),
    url(r'^habits/', include('habits.urls', namespace="habits")),
    url(r'^tags/', include('tags.urls', namespace="tags")),

    url(r'^features/', include('features.urls', namespace="features")),
    url(r'^commands/', include('commands.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# remove group model from admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)
