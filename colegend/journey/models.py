from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import AutoOwnedBase, TimeStampedBase


class Hero(AutoOwnedBase, TimeStampedBase):
    content = MarkdownField()

    class Meta:
        verbose_name = _('Hero')
        verbose_name_plural = _('Heroes')
        default_related_name = 'hero'

    def __str__(self):
        return "{}'s hero".format(self.owner)


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
