from django.contrib import admin
from .models import Connected


@admin.register(Connected)
class ConnectedAdmin(admin.ModelAdmin):
    pass
