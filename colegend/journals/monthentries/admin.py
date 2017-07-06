from django.contrib import admin
from .models import MonthEntry


@admin.register(MonthEntry)
class MonthEntryAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']
    list_display = ['date', 'journal']
    list_filter = ['journal__owner']
