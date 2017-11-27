from django.contrib import admin
from .models import Scan


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner']
    list_filter = ['owner', 'date']
    readonly_fields = ['created']
