from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, Q
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase, OwnedBase
from django.utils.translation import ugettext_lazy as _

from colegend.scopes.models import ScopeField


class AdventureTag(models.Model):
    """
    A django model representing an adventures's text-tag.
    """
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']
        default_related_name = 'tags'

    def __str__(self):
        return self.name


class AdventureQuerySet(models.QuerySet):
    def search(self, query):
        queryset = self.filter(Q(name__icontains=query) | Q(content__icontains=query))
        return queryset


class Adventure(TimeStampedBase):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )
    scope = ScopeField(
    )
    public = models.BooleanField(
        default=False
    )
    image_url = models.URLField(
        _('image url'),
        blank=True
    )
    content = MarkdownField(
        blank=True
    )
    tags = models.ManyToManyField(
        to=AdventureTag,
        blank=True,
    )
    notes = models.TextField(
        verbose_name=_("notes"),
        help_text=_("Staff notes."),
        blank=True
    )
    adventurers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='AdventureReview'
    )

    @property
    def rating(self):
        return self.adventure_reviews.aggregate(Avg('rating')).get('rating__avg') or 0

    objects = AdventureQuerySet.as_manager()

    class Meta:
        default_related_name = 'adventures'
        ordering = ['name']

    def __str__(self):
        return self.name


class AdventureReview(OwnedBase, TimeStampedBase):
    adventure = models.ForeignKey(
        to=Adventure,
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        _('rating'),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    content = MarkdownField(
        blank=True
    )
    image_url = models.URLField(
        _('image url'),
        blank=True
    )

    class Meta:
        default_related_name = 'adventure_reviews'
        unique_together = ['owner', 'adventure']

    def __str__(self):
        return '{adventure}/{user}'.format(adventure=self.adventure, user=self.owner)


class ArcadePage(Page):
    template = 'arcade/base.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['AdventuresPage', 'GamesPage', 'ContestsPage', 'ShopPage']


class AdventuresPage(Page):
    template = 'arcade/adventures.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class GamesPage(Page):
    template = 'arcade/games.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class ContestsPage(Page):
    template = 'arcade/contests.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class ShopPage(Page):
    template = 'arcade/shop.html'

    parent_page_types = ['ArcadePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title
