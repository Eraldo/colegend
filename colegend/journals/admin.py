from django.contrib import admin
from journals.models import DayEntry


class DayEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner']
    search_fields = ['text']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['date', 'text']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(DayEntry, DayEntryAdmin)
