from django.contrib import admin

from colegend.office.models import Focus


@admin.register(Focus)
class FocusAdmin(admin.ModelAdmin):
    list_display = ['scope', 'start', 'end', 'owner']
    list_filter = ['scope', 'owner']
