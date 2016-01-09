from django.contrib import admin
from orderable.admin import OrderableAdmin
from .models import Card, Checkpoint, Game


@admin.register(Card)
class CardAdmin(OrderableAdmin):
    pass


@admin.register(Checkpoint)
class CheckpointAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ['hand', 'completed', 'checkpoints']
