from django.contrib import admin

# Register your models here.
from dojo.models import Module, Category

__author__ = 'eraldo'


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'accepted', 'provider']
    list_filter = ['category']


admin.site.register(Module, ModuleAdmin)
admin.site.register(Category)
