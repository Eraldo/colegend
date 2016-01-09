from django.contrib import admin
from .models import Checkpoint, Game


@admin.register(Checkpoint)
class CheckpointAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ['hand', 'completed', 'checkpoints']
