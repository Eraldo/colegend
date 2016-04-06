from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass
