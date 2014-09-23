from django.contrib import admin
from features.models import Feature

__author__ = 'eraldo'


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_published', 'role']
    list_filter = ['role']
    search_fields = ['name']
admin.site.register(Feature, FeatureAdmin)
