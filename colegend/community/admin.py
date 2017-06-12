from django.contrib import admin

from colegend.users.admin import UserInline
from .models import Tribe, Clan, Duo


@admin.register(Duo)
class DuoAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [UserInline]


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [UserInline]


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [UserInline]
