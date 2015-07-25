from django.contrib import admin
from cards.models import Card, Deck


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'deck']
    list_filter = ['deck']


admin.site.register(Card, CardAdmin)
admin.site.register(Deck)
