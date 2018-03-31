from django.contrib import admin
from .models import Hero, Demon, Quote


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_filter = ['owner']


@admin.register(Demon)
class DemonAdmin(admin.ModelAdmin):
    list_filter = ['owner']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'used_as_daily', 'provider', 'accepted']
    list_filter = ['accepted', 'categories', 'provider']
    filter_horizontal = ['categories']
