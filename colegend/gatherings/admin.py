from django.contrib import admin
from gatherings.models import Gathering


class GatheringAdmin(admin.ModelAdmin):
    list_display = ['date', 'location', 'online', 'host']
    list_filter = ['online', 'host']


admin.site.register(Gathering, GatheringAdmin)