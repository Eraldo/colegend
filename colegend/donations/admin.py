from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'owner']
    list_filter = ['date', 'owner']
