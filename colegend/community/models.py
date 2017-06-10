from django.db import models
from django.db.models import Count
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.wagtailcore.models import Page

from colegend.journals.scopes import Day


class CommunityPage(RoutablePageMixin, Page):
    template = 'community/base.html'

    class Meta:
        verbose_name = _('community')
        verbose_name_plural = _('communities')

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['DuoPage', 'ClanPage', 'TribePage', 'MentorPage']


class DuoPage(Page):
    template = 'community/duo.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        user = request.user
        if user.is_authenticated:
            duo = user.duo
            if duo:
                context['duo'] = duo
                context['scope'] = Day()
        return context

    def __str__(self):
        return self.title


class ClanPage(Page):
    template = 'community/clan.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class TribePage(Page):
    template = 'community/tribe.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class MentorPage(Page):
    template = 'community/mentor.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    def __str__(self):
        return self.title


class TribeQuerySet(models.QuerySet):
    pass


class Tribe(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new tribe')
    )

    objects = TribeQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'tribes'


class Clan(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new clan'),
    )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'clans'


class DuoQuerySet(models.QuerySet):
    def open(self):
        return self.annotate(member_count=Count('members')).filter(member_count__lte=1).order_by('-member_count')


class Duo(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new duo')
    )

    objects = DuoQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'duos'
