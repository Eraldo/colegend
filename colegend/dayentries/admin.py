from django.contrib import admin
from .models import DayEntry


@admin.register(DayEntry)
class DayEntryAdmin(admin.ModelAdmin):
    pass
