from django.contrib import admin
from .models import YearEntry


@admin.register(YearEntry)
class YearEntryAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']
