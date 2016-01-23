from django.contrib import admin
from .models import InnerCall


@admin.register(InnerCall)
class InnerCallAdmin(admin.ModelAdmin):
    pass
