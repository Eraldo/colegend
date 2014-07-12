from django.contrib import admin
from habits.admin import HabitInline
from routines.models import Routine

__author__ = 'eraldo'


class RoutineAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    search_fields = ['name', 'description']
    list_filter = ['type', 'tags']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['type', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
        ]
    inlines = [HabitInline]
admin.site.register(Routine, RoutineAdmin)