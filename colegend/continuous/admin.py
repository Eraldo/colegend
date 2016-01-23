from django.contrib import admin
from .models import Continuous


@admin.register(Continuous)
class ContinuousAdmin(admin.ModelAdmin):
    pass
