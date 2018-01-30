from django.db import models
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoOwnedBase, TimeStampedBase


class Hero(AutoOwnedBase, TimeStampedBase):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        blank=True
    )
    avatar = models.URLField(
        _('avatar'),
        max_length=1000,
        blank=True
    )
    values = MarkdownField(blank=True)
    powers = MarkdownField(blank=True)
    skills = MarkdownField(blank=True)
    habits = MarkdownField(blank=True)
    principles = MarkdownField(blank=True)
    wishes = MarkdownField(blank=True)
    goals = MarkdownField(blank=True)
    people = MarkdownField(blank=True)
    resources = MarkdownField(blank=True)
    achievements = MarkdownField(blank=True)
    questions = MarkdownField(blank=True)
    experiments = MarkdownField(blank=True)
    projects = MarkdownField(blank=True)
    bucket = MarkdownField(blank=True, help_text="bucket list")
    content = MarkdownField(blank=True)

    class Meta:
        verbose_name = _('Hero')
        verbose_name_plural = _('Heroes')
        default_related_name = 'hero'

    def __str__(self):
        return "{}'s hero".format(self.owner)


class Demon(AutoOwnedBase, TimeStampedBase):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        blank=True
    )
    avatar = models.URLField(
        _('avatar'),
        max_length=1000,
        blank=True
    )
    tensions = MarkdownField(blank=True)
    fears = MarkdownField(blank=True)
    content = MarkdownField(blank=True)

    class Meta:
        verbose_name = _('Demon')
        verbose_name_plural = _('Demons')
        default_related_name = 'demon'

    def __str__(self):
        return "{}'s demon".format(self.owner)


class JourneyPage(Page):
    template = 'journey/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['QuestPage', 'HeroPage', 'DemonPage', 'AchievementsPage']


class QuestPage(Page):
    template = 'journey/quest.html'

    parent_page_types = ['JourneyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        user = request.user
        context['experience'] = user.experience.total()
        return context

    def __str__(self):
        return self.title


class HeroPage(Page):
    template = 'journey/hero.html'

    parent_page_types = ['JourneyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class DemonPage(Page):
    template = 'journey/demon.html'

    parent_page_types = ['JourneyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class AchievementsPage(Page):
    template = 'journey/achievements.html'

    parent_page_types = ['JourneyPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
