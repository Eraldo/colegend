from django.contrib import admin

# Register your models here.
from .models import Legend


@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    pass
