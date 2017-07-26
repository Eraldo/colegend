from django.contrib import admin
from .models import Journal, JournalEntry


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['scope', 'start', 'owner']
    list_filter = ['scope', 'owner']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass
