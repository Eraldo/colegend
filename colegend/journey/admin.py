from django import forms
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline

from .models import Hero, Demon, Quote, Quest, QuestObjective, UserQuestStatus


class QuestObjectiveInline(OrderedTabularInline):
    model = QuestObjective
    fields = ['name', 'code', 'order', 'move_up_down_links']
    readonly_fields = ['order', 'move_up_down_links']
    show_change_link = True
    extra = 1
    ordering = ['order']


@admin.register(Quest)
class QuestAdmin(OrderedModelAdmin):
    list_display = ['name', 'move_up_down_links']
    inlines = [QuestObjectiveInline]

    def get_urls(self):
        urls = super().get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls


# @admin.register(QuestObjective)
# class QuestObjectiveAdmin(admin.ModelAdmin):
#     list_display = ['name', 'code', 'quest']
#     list_filter = ['quest']


class UserQuestStatusForm(forms.ModelForm):
    class Meta:
        model = UserQuestStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['completed_objectives'].queryset = self.fields['completed_objectives'].queryset \
            .filter(quest=self.instance.quest)
        print(self.fields['completed_objectives'].queryset)


@admin.register(UserQuestStatus)
class UserQuestStatusAdmin(admin.ModelAdmin):
    form = UserQuestStatusForm
    list_filter = ['owner', 'quest', 'completed_objectives']
    filter_horizontal = ['completed_objectives']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if 'completed_objectives' in self.initial:
    #         self.fields['completed_objectives'].queryset = QuestObjective.objects.filter(Q(pk__in=self.initial['event_dates']) | Q(event_date__gte=date.today()))
    #     else:
    #         self.fields['event_dates'].queryset = EventDate.objects.filter(event_date__gte=date.today())


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_filter = ['owner']


@admin.register(Demon)
class DemonAdmin(admin.ModelAdmin):
    list_filter = ['owner']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'used_as_daily', 'provider', 'accepted']
    list_filter = ['accepted', 'categories', 'provider']
    search_fields = ['name', 'author']
    filter_horizontal = ['categories', 'liked_by', 'disliked_by']
