from django.contrib import admin
from .models import Conscious


@admin.register(Conscious)
class ConsciousAdmin(admin.ModelAdmin):
    pass
