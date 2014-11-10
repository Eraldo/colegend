from django.contrib import admin
from news.models import NewsBlock


class NewsBlockAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'owner']


admin.site.register(NewsBlock, NewsBlockAdmin)
