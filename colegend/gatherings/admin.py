from django.contrib import admin
from gatherings.models import Gathering


class GatheringAdmin(admin.ModelAdmin):
    list_display = ['start', 'end', 'location', 'online', 'topic', 'host', ]
    list_filter = ['online', 'host']


admin.site.register(Gathering, GatheringAdmin)
