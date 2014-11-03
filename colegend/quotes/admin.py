from django.contrib import admin

# Register your models here.
from quotes.models import Quote, Category


def accept(modeladmin, request, queryset):
    queryset.update(accepted=True)


accept.short_description = "Accept selected quotes."


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'accepted', 'used_as_daily', 'provider']
    list_filter = ['category', 'author']
    actions = [accept]


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Category)
