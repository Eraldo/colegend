from django.contrib import admin
from projects.models import Project
from tasks.admin import TaskInline

__author__ = 'eraldo'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline']
    search_fields = ['name', 'description']
    list_filter = ['status', 'tags']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        # (None, {'fields': ['reason', 'outcome']}),
        (None, {'fields': ['status', 'deadline', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
        ]
    # filter_horizontal = ("members",)
    inlines = [TaskInline]
admin.site.register(Project, ProjectAdmin)