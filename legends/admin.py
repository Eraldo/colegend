from django.contrib import admin
from .models import Legend


@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    pass
