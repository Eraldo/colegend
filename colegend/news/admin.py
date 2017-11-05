from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'author']
    list_filter = ['date', 'author']
    readonly_fields = ['created']
