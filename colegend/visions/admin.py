from django.contrib import admin
from .models import Vision


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    pass
