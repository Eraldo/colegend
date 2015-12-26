from django.contrib import admin
from .models import OuterCall


@admin.register(OuterCall)
class OuterCallAdmin(admin.ModelAdmin):
    pass
