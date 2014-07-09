from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()

# remove group model from admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # main urls
    url(r'', include('home.urls')),
    url(r'', include('website.urls')),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^tasks/', include('tasks.urls', namespace="tasks")),
    url(r'^tags/', include('tags.urls', namespace="tags")),

    url(r'^commands/', include('commands.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
