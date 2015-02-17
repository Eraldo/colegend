from django.contrib import admin
from tasks.models import Task
from lib.admin import InlineMixin

__author__ = 'eraldo'


class TaskInline(InlineMixin, admin.TabularInline):
    model = Task
    fields = ['name', 'status', 'date', 'deadline', 'tags', 'category', 'owner', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline', 'date', 'category', 'project', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['status', 'tags', 'category', 'owner']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'completion_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner', 'project']}),
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['status', 'deadline', 'date', 'tags', 'category']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'completion_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Task, TaskAdmin)
