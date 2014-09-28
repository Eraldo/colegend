from django.contrib import admin

# Register your models here.
from quotes.models import Quote, Category


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'accepted', 'provider']
    list_filter = ['category', 'author']


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Category)
