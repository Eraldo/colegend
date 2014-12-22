from django.contrib import admin
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerField
from easy_thumbnails.widgets import ImageClearableFileInput
from features.models import Feature

__author__ = 'eraldo'


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_published', 'role']
    list_filter = ['role']
    search_fields = ['name']

    # formfield_overrides = {
    #     ThumbnailerField: {'widget': ImageClearableFileInput},
    # }

    # def thumbnail(self, value):
    #     image = value.image
    #     if image:
    #             return '<img src="{}{}" />'.format(settings.MEDIA_URL, image)
    #     else:
    #         return ''
    # thumbnail.allow_tags = True

admin.site.register(Feature, FeatureAdmin)
