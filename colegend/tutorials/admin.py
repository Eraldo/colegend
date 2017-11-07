from django.contrib import admin
from .models import Tutorial


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = []
    readonly_fields = ['created']
