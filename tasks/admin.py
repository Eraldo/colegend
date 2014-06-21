from django.contrib import admin
from lib.admin import InlineMixin
from tasks.models import Task

__author__ = 'eraldo'


class TaskInline(InlineMixin, admin.TabularInline):
    fields = ['name', 'status', 'date', 'deadline', 'tags', 'history', 'change_link']
    model = Task
    extra = 0
    readonly_fields = ('change_link',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'project']
    search_fields = ['name', 'description']
    list_filter = ['status']
    readonly_fields = ['creation_date', 'modification_date']
admin.site.register(Task, TaskAdmin)