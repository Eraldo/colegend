from django.contrib import admin
from taggit.admin import TagAdmin
from tags.models import Tag
from taggit.models import Tag as TaggitTag

__author__ = 'eraldo'


admin.site.unregister(TaggitTag)
admin.site.register(Tag, TagAdmin)
