from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'end', 'location']
    list_filter = ['start', 'end', 'location']
    readonly_fields = ['created']
