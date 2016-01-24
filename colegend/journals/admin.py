from django.contrib import admin
from .models import Journal


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass
