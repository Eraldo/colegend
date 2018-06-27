from django.contrib import admin
from django.db.models import Count

from .models import Role, Circle


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname', 'item', 'users_count', 'circle']
    list_filter = ['circle', 'users']
    search_fields = ['name', 'nickname', 'item', 'description']

    def get_queryset(self, request):
        """
        Annotating the queryset to prevent extra queries for many to many counts.
        :param request:
        :return: Annotated queryset
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _users_count=Count('users', distinct=True),
        )
        return queryset

    def users_count(self, obj):
        return obj._users_count

    users_count.short_description = 'Users'


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'purpose', 'strategy']
