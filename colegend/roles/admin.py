from django.contrib import admin
from .models import Role, Circle


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    pass
