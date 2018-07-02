from django.contrib import admin
from .models import Outcome, Step


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'scope', 'score', 'comparisons', 'owner']
    list_filter = ['status', 'scope', 'owner', 'tags', 'related_outcomes']
    filter_horizontal = ['tags', 'related_outcomes']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'outcome']
    # list_filter = ['owner']
