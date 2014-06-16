from django.contrib import admin
from tasks.models import Task

__author__ = 'eraldo'


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'project']
    search_fields = ['name']
    list_filter = ['status']
admin.site.register(Task, TaskAdmin)