from django.conf.urls import patterns, include, url

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
    url(r'^projects/', include('projects.urls', namespace="projects")),

    url(r'^admin/', include(admin.site.urls)),
)
