from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from challenges.models import Challenge

__author__ = 'eraldo'


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'accepted', 'provider']
    list_filter = ['category']


admin.site.register(Challenge, ChallengeAdmin)
