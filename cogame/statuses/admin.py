from django.contrib import admin
from statuses.models import Status

__author__ = 'Eraldo Helal'


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'order']
    search_fields = ['name']
    list_filter = ['type']
admin.site.register(Status, StatusAdmin)
