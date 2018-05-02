from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedModelAdmin

from .models import Scan, Habit, HabitTrackEvent, HabitReminder, RoutineHabit, Routine


class HabitTrackEventInlineAdmin(admin.TabularInline):
    model = HabitTrackEvent
    fields = ['created']
    readonly_fields = ['created']
    extra = 0


# @admin.register(HabitTrackEvent)
# class HabitTrackEventAdmin(admin.ModelAdmin):
#     list_display = ['created', 'habit']
#     list_filter = ['habit']
#     readonly_fields = ['created']


class HabitReminderInlineAdmin(admin.TabularInline):
    model = HabitReminder
    fields = ['time']
    extra = 0


# @admin.register(HabitReminder)
# class HabitReminderAdmin(admin.ModelAdmin):
#     list_display = ['time', 'habit']
#     list_filter = ['habit']
#     readonly_fields = ['created']


@admin.register(Habit)
class HabitAdmin(OrderedModelAdmin):
    list_display = ['name', 'scope', 'duration', 'is_active', 'is_controlled', 'owner', 'streak', 'streak_max', 'order', 'move_up_down_links']
    list_filter = ['scope', 'owner']
    readonly_fields = ['created', 'order']
    inlines = [HabitReminderInlineAdmin, HabitTrackEventInlineAdmin]


class RoutineHabitInlineAdmin(OrderedTabularInline):
    model = RoutineHabit
    fields = ['habit', 'order', 'move_up_down_links']
    readonly_fields = ['order', 'move_up_down_links']
    extra = 1
    ordering = ['order']


@admin.register(Routine)
class RoutineAdmin(OrderedModelAdmin):
    list_display = ['name', 'scope', 'owner', 'order', 'move_up_down_links']
    list_filter = ['scope', 'owner']
    readonly_fields = ['created', 'order']
    inlines = [RoutineHabitInlineAdmin]

    def get_urls(self):
        urls = super().get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner']
    list_filter = ['owner', 'date']
    readonly_fields = ['created']
