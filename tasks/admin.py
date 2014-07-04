from django.contrib import admin
from lib.admin import InlineMixin
from tasks.models import Task

__author__ = 'eraldo'


class TaskInline(InlineMixin, admin.TabularInline):
    model = Task
    fields = ['name', 'status', 'date', 'deadline', 'tags', 'history', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline', 'date', 'project']
    search_fields = ['name', 'description']
    list_filter = ['status', 'tags']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['project']}),
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['status', 'deadline', 'date', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Task, TaskAdmin)