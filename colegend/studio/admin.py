from django.contrib import admin
from .models import InterviewEntry


@admin.register(InterviewEntry)
class InterviewEntryAdmin(admin.ModelAdmin):
    list_display = ['scope', 'start', 'owner']
    list_filter = ['scope', 'owner']
