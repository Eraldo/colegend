from django.contrib import admin
from projects.models import Project

__author__ = 'eraldo'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Project, ProjectAdmin)