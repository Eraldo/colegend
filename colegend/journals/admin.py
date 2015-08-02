from django.contrib import admin
from journals.models import DayEntry, Journal, WeekEntry
from lib.admin import InlineMixin


class DayEntryInline(InlineMixin, admin.TabularInline):
    model = DayEntry
    fields = ['date', 'location', 'focus', 'journal', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class DayEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'focus', 'journal']
    search_fields = ['focus', 'content']
    list_filter = ['journal']
    readonly_fields = ['creation_date', 'modification_date', 'history']
    filter_horizontal = ['tags']

    fieldsets = [
        (None, {'fields': ['journal']}),
        (None, {'fields': ['date', 'location', 'focus', 'content', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(DayEntry, DayEntryAdmin)


class WeekEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'focus', 'journal']
    search_fields = ['focus', 'content']
    list_filter = ['journal']
    readonly_fields = ['creation_date', 'modification_date', 'history']
    filter_horizontal = ['tags']

    fieldsets = [
        (None, {'fields': ['journal']}),
        (None, {'fields': ['date', 'focus', 'content', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(WeekEntry, WeekEntryAdmin)


class JournalAdmin(admin.ModelAdmin):
    inlines = [DayEntryInline]


admin.site.register(Journal, JournalAdmin)
