from django.contrib import admin
from features.models import Feature

__author__ = 'eraldo'


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_published']
    search_fields = ['name']
admin.site.register(Feature, FeatureAdmin)