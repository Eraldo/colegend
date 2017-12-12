from django.contrib import admin
from .models import Adventure, AdventureTag


@admin.register(AdventureTag)
class AdventureTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ['name', 'scope']
    list_filter = ['public', 'scope', 'tags']
    filter_horizontal = ['tags']
    readonly_fields = ['created']
