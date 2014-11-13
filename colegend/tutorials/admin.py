from django.contrib import admin
from tutorials.models import Tutorial

__author__ = 'eraldo'


class TutorialAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Tutorial, TutorialAdmin)
