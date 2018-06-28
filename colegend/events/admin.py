from django.contrib import admin
from django.db.models import Count

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'end', 'location', 'participants_count']
    list_filter = ['start', 'end', 'location', 'participants']
    filter_horizontal = ['participants']
    readonly_fields = ['created']

    def get_queryset(self, request):
        """
        Annotating the queryset to prevent extra queries for many to many counts.
        :param request:
        :return: Annotated queryset
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _participants_count=Count('participants', distinct=True),
        )
        return queryset

    def participants_count(self, obj):
        return obj._participants_count

    participants_count.short_description = 'Participants'
    participants_count.admin_order_field = '_participants_count'
