from django.contrib import admin
from .models import Role, Circle


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname', 'item']
    search_fields = ['name', 'nickname', 'item', 'description']


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'purpose', 'strategy']
