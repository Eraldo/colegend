from django.contrib import admin
from .models import Tribe, Clan, Duo


@admin.register(Duo)
class DuoAdmin(admin.ModelAdmin):
    list_display = ['name', 'clan']
    list_filter = ['clan__tribe__mentor', 'clan__tribe']


class DuoInline(admin.TabularInline):
    model = Duo
    max_num = 2
    extra = 2


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ['name', 'tribe']
    inlines = [DuoInline]
    list_filter = ['tribe__mentor']


class ClanInline(admin.TabularInline):
    model = Clan
    max_num = 4
    extra = 4


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ['name', 'mentor']
    inlines = [ClanInline]
