from django.contrib import admin
from trackers.models import Weight, Joke, Book, Sex


class WeightAdmin(admin.ModelAdmin):
    list_display = ['time', 'weight', 'owner']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['time', 'weight', 'notes']}),
        ('history', {'fields': ['creation_date', 'modification_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Weight, WeightAdmin)


class SexAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'person', 'owner']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['date', 'amount', 'person', 'notes']}),
        ('history', {'fields': ['creation_date', 'modification_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Sex, SexAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'has_url', 'owner']
    list_filter = ['owner']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['title', 'author', 'status', 'url', 'notes']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Book, BookAdmin)


class JokeAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'owner']
    list_filter = ['owner', 'rating']
    readonly_fields = ['creation_date', 'modification_date']

    fieldsets = [
        (None, {'fields': ['owner']}),
        (None, {'fields': ['name', 'description', 'rating']}),
        ('history', {'fields': ['creation_date', 'modification_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Joke, JokeAdmin)
