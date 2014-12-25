from django.contrib import admin
from notifications.models import Notification

__author__ = 'eraldo'


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'creation_date']
    search_fields = ['name']
    list_filter = ['owner', 'read']
    readonly_fields = ['creation_date', 'modification_date']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'description', 'read']}),
        ('history', {'fields': ['creation_date', 'modification_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Notification, NotificationAdmin)
