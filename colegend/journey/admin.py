from django.contrib import admin
from .models import Hero, Demon, Quote


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass


@admin.register(Demon)
class DemonAdmin(admin.ModelAdmin):
    pass


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass
