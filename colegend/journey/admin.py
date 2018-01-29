from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass
