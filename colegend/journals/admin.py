from django.contrib import admin
from journals.models import DayEntry, Journal
from lib.admin import InlineMixin


class DayEntryInline(InlineMixin, admin.TabularInline):
    model = DayEntry
    fields = ['date', 'location', 'focus', 'owner', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class DayEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'focus', 'journal']
    search_fields = ['focus', 'content']
    list_filter = ['journal', 'location']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['journal']}),
        (None, {'fields': ['date', 'location', 'focus', 'content']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(DayEntry, DayEntryAdmin)


class JournalAdmin(admin.ModelAdmin):
    inlines = [DayEntryInline]


admin.site.register(Journal, JournalAdmin)
