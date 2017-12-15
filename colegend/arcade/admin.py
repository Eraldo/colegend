from django.contrib import admin
from .models import Adventure, AdventureTag, AdventureReview


@admin.register(AdventureTag)
class AdventureTagAdmin(admin.ModelAdmin):
    pass


class AdventureReviewInline(admin.TabularInline):
    model = AdventureReview
    extra = 0


@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ['name', 'scope', 'level', 'public']
    list_filter = ['public', 'scope', 'tags', 'level']
    list_editable = ['public']
    filter_horizontal = ['tags']
    readonly_fields = ['created']
    inlines = [AdventureReviewInline]
