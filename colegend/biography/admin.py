from django.contrib import admin
from .models import Biography


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    pass
