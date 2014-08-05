from django.contrib import admin
from django.core.urlresolvers import reverse
from lib.admin import InlineMixin
from tags.models import Tag

__author__ = 'eraldo'


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'description']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]
    # TODO: inlines = [TaskInline, etc]


admin.site.register(Tag, TagAdmin)
