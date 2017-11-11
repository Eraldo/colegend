from django.contrib import admin
from .models import InterviewEntry, Chapter, Story


@admin.register(InterviewEntry)
class InterviewEntryAdmin(admin.ModelAdmin):
    list_display = ['scope', 'start', 'owner']
    list_filter = ['scope', 'owner']
    readonly_fields = ['created']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'story__owner']
    list_filter = ['story__owner']
    readonly_fields = ['created']

    def story__owner(self, obj):
        return obj.story.owner
