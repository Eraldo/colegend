from django.contrib import admin
from .models import Outcome


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    pass
