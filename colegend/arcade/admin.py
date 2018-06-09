from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedModelAdmin

from .models import Adventure, AdventureTag, AdventureReview, Card, Deck


@admin.register(AdventureTag)
class AdventureTagAdmin(admin.ModelAdmin):
    pass


class AdventureReviewInline(admin.TabularInline):
    model = AdventureReview
    extra = 0


@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ['name', 'scope', 'level', 'public']
    list_filter = ['public', 'scope', 'tags', 'level']
    list_editable = ['public']
    filter_horizontal = ['tags']
    readonly_fields = ['created']
    inlines = [AdventureReviewInline]


class CardInlineAdmin(OrderedTabularInline):
    model = Card
    fields = ['name', 'image', 'content', 'notes', 'order', 'move_up_down_links']
    readonly_fields = ['order', 'move_up_down_links']
    extra = 0
    ordering = ['order']


@admin.register(Card)
class CardAdmin(OrderedModelAdmin):
    pass


@admin.register(Deck)
class DeckAdmin(OrderedModelAdmin):
    list_display = ['name']
    inlines = [CardInlineAdmin]

    def get_urls(self):
        urls = super().get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls
