from django.contrib import admin
from .models import WeekEntry


@admin.register(WeekEntry)
class WeekEntryAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']
