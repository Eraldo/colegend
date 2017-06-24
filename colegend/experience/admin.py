from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['created', 'app', 'level', 'amount', 'owner']
    list_filter = ['owner', 'app', 'level']
    readonly_fields = ['created']
