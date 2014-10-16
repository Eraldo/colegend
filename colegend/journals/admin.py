from django.contrib import admin
from journals.models import DayEntry


class DayEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'focus', 'owner']
    search_fields = ['focus', 'text']
    list_filter = ['owner', 'location']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['date', 'location', 'focus', 'text']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(DayEntry, DayEntryAdmin)
