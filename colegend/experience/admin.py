from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['created', 'action', 'amount', 'owner']
    list_filter = ['owner', 'action']
    readonly_fields = ['created']
