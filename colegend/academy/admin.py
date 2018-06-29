from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Book, BookReview, BookTag


class TaggedBookInline(admin.TabularInline):
    verbose_name = _('tagged book')
    verbose_name_plural = _('tagged books')
    model = Book.tags.through
    extra = 0
    show_change_link = True


class BookReviewInline(admin.TabularInline):
    fields = ['owner', 'rating', 'area_1', 'area_2', 'area_3', 'area_4', 'area_5', 'area_6', 'area_7']
    model = BookReview
    extra = 0
    show_change_link = True


@admin.register(BookTag)
class BookTagAdmin(admin.ModelAdmin):
    inlines = [TaggedBookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'rating', 'public', 'featured']
    list_filter = ['public', 'featured', 'tags']
    list_editable = ['public']
    filter_horizontal = ['tags']
    readonly_fields = ['created']
    search_fields = ['name', 'author']
    inlines = [BookReviewInline]


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'owner']
    list_filter = ['owner', 'book']
    readonly_fields = ['created']
