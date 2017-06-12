from django.contrib import admin

from colegend.welcome.models import WaitingUser


@admin.register(WaitingUser)
class WaitingUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'created', 'informed', 'accepted']
    readonly_fields = ['created', 'modified']
