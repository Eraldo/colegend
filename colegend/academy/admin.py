from django.contrib import admin
from .models import Book, BookReview


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'featured']
    list_filter = ['featured']
    readonly_fields = ['created']


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'owner']
    list_filter = ['owner', 'book']
    readonly_fields = ['created']
