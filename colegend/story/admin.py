from django.contrib import admin
from .models import WelcomeTreeLeaf


@admin.register(WelcomeTreeLeaf)
class WelcomeTreeLeafAdmin(admin.ModelAdmin):
    pass
