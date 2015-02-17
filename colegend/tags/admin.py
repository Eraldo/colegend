from django.contrib import admin
from tags.models import Tag

__author__ = 'eraldo'


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['category', 'owner']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'description', 'category']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Tag, TagAdmin)
