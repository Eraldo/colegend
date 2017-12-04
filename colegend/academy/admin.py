from django.contrib import admin
from .models import Book, BookReview, BookTag


class BookReviewInline(admin.TabularInline):
    fields = ['owner', 'rating', 'area_1', 'area_2', 'area_3', 'area_4', 'area_5', 'area_6', 'area_7']
    model = BookReview
    extra = 0


@admin.register(BookTag)
class BookTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'featured']
    list_filter = ['featured', 'public', 'tags']
    readonly_fields = ['created']
    inlines = [BookReviewInline]


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'owner']
    list_filter = ['owner', 'book']
    readonly_fields = ['created']


