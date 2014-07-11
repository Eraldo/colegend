from django.contrib import admin
from habits.models import Habit
from lib.admin import InlineMixin

__author__ = 'eraldo'


class HabitInline(InlineMixin, admin.TabularInline):
    model = Habit
    fields = ['name', 'tags', 'history', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class HabitAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']
    list_filter = ['tags']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Habit, HabitAdmin)