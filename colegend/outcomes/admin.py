from django.contrib import admin
from .models import Outcome


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'scope', 'owner']
    list_filter = ['scope', 'owner']
