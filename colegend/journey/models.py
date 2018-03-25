from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page

from colegend.categories.models import Category
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
    inspirations = MarkdownField(blank=True)
    content = MarkdownField(blank=True)
    routines = MarkdownField(blank=True)

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


class QuoteQuerySet(models.QuerySet):
    def accepted(self):
        return self.filter(accepted=True)

    def pending(self):
        return self.filter(accepted=False)

    def random(self):
        return self.accepted().order_by('?').first()

    def owned_by(self, user):
        return self.filter(provider=user)

    def daily_quote(self, date=None):
        # Use only accepted quotes.
        quotes = self.accepted()

        # Fetch past quote if a date was given.
        if date:
            try:
                return quotes.get(used_as_daily=date)
            except Quote.DoesNotExist:
                return None

        # Get or assign today's quote:
        # Check if there already is a quote for today
        # If not..
        # then assign one using a 'new' quote.
        # If there are no new ones..
        # then use the last used quote.

        today = timezone.now().date()
        try:
            current_quote = quotes.get(used_as_daily=today)
        except Quote.DoesNotExist:
            # There is no quote for today yet.. so assign one.
            current_quote = quotes.order_by('used_as_daily').first()
            if current_quote:
                current_quote.used_as_daily = today
                current_quote.save()
        return current_quote


class Quote(TimeStampedBase):
    """A motivational quote."""

    name = models.CharField(
        verbose_name=_("name"),
        max_length=255,
        unique=True,
        help_text=_("What is the quote about?")
    )
    content = MarkdownField(blank=True)
    author = models.CharField(
        verbose_name=_('author'),
        max_length=255,
        blank=True
    )
    categories = models.ManyToManyField(
        verbose_name=_('categories'),
        to=Category
    )
    provider = models.ForeignKey(
        verbose_name=_('provider'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    accepted = models.BooleanField(
        verbose_name=_('accepted'),
        default=False
    )
    used_as_daily = models.DateField(
        null=True, blank=True,
        unique=True
    )

    objects = QuoteQuerySet.as_manager()

    def __str__(self):
        return self.name

    @property
    def pending(self):
        return not self.accepted

    def accept(self, save=True):
        self.accepted = True
        if save:
            self.save()
        # Notify user
        if self.provider:
            self.provider.contact(subject='Your quote "{}" has been accepted. EOM'.format(self.name))

    class Meta:
        default_related_name = 'quotes'


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
