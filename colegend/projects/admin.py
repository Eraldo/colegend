from django.contrib import admin
from projects.models import Project
from tasks.admin import TaskInline

__author__ = 'eraldo'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline', 'date', 'category', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['status', 'tags', 'category', 'owner']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'completion_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['status', 'deadline', 'date', 'tags', 'category']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'completion_date', 'history'], 'classes': ['collapse']}),
    ]
    inlines = [TaskInline]


admin.site.register(Project, ProjectAdmin)
