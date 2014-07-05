from django.contrib import admin
from django.core.urlresolvers import reverse
from lib.admin import InlineMixin
from tags.models import Tag

__author__ = 'eraldo'


class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)
