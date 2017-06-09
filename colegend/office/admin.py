from django.contrib import admin

from colegend.office.models import Focus


@admin.register(Focus)
class FocusAdmin(admin.ModelAdmin):
    pass
