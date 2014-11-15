from django.contrib import admin
from visions.models import Vision

__author__ = 'eraldo'


class VisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    search_fields = ['name', 'content']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'content']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]

admin.site.register(Vision, VisionAdmin)
