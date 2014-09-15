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

    # operator
    url(r'', include('website.urls')),
    url(r'^legend/', include('legend.urls', namespace="legend")),
    url(r'^features/', include('features.urls', namespace="features")),
    url(r'^commands/', include('commands.urls')),
    url(r'^contact/', include('contact.urls')),
    # manager
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^tasks/', include('tasks.urls', namespace="tasks")),
    url(r'^routines/', include('routines.urls', namespace="routines")),
    url(r'^habits/', include('habits.urls', namespace="habits")),
    url(r'^tags/', include('tags.urls', namespace="tags")),
    # mentor
    url(r'^visions/', include('visions.urls', namespace="visions")),
    url(r'^journals/', include('journals.urls', namespace="journals")),
    url(r'^meetings/', include('meetings.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^backend/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# remove group model from admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)
