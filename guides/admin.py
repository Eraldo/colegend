from django.contrib import admin
from .models import GuideRelation


@admin.register(GuideRelation)
class GuideRelationAdmin(admin.ModelAdmin):
    pass
