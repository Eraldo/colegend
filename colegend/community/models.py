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
    #
    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     from colegend.users.models import User
    #     context['legends'] = User.objects.filter(is_active=True)
    #     context['tribes'] = Tribe.objects.all()
    #     context['clans'] = Clan.objects.all()
    #     context['duos'] = Duo.objects.all()
    #     return context
    #
    # def render(self, request, template=None, context=None):
    #     request.is_preview = getattr(request, 'is_preview', False)
    #     return TemplateResponse(
    #         request,
    #         template or self.get_template(request),
    #         context or self.get_context(request)
    #     )
    #
    # @route(r'^$')
    # def index(self, request):
    #     return self.render(request)
    #
    # @route(r'^duo/$')
    # def duo(self, request):
    #     context = self.get_context(request)
    #     user = request.user
    #     if user.is_authenticated():
    #         duo = user.duo
    #         if duo:
    #             partner = duo.members.exclude(id=user.id).first()
    #             if partner:
    #                 context['partner'] = partner
    #                 dayentry = partner.journal.dayentries.current().first()
    #                 if dayentry:
    #                     partner.focus = format_html_join('', '{0} [{1}]<br>', ((outcome, outcome.get_status_display()) for outcome in dayentry.outcomes))
    #         context['duo'] = user.duo
    #     return self.render(request, template='community/duo.html', context=context)
    #
    # @route(r'^clan/$')
    # def clan(self, request):
    #     context = self.get_context(request)
    #     user = request.user
    #     if user.is_authenticated():
    #         duo = user.duo
    #         if duo:
    #             clan = duo.clan
    #             if clan:
    #                 context['clan'] = clan
    #                 partners = clan.members.exclude(id=user.id)
    #                 if partners:
    #                     context['partners'] = partners
    #                     for partner in partners:
    #                         weekentry = partner.journal.weekentries.current().first()
    #                         if weekentry:
    #                             partner.focus = format_html_join('', '{0} [{1}]<br>',
    #                                                              ((outcome, outcome.get_status_display()) for outcome in
    #                                                               weekentry.outcomes))
    #     return self.render(request, template='community/clan.html', context=context)
    #
    # @route(r'^tribe/$')
    # def tribe(self, request):
    #     context = self.get_context(request)
    #     user = request.user
    #     if user.is_authenticated():
    #         duo = user.duo
    #         if duo:
    #             clan = duo.clan
    #             if clan:
    #                 tribe = clan.tribe
    #                 if tribe:
    #                     context['tribe'] = tribe
    #                     partners = tribe.members.exclude(id=user.id)
    #                     if partners:
    #                         context['partners'] = partners
    #                         for partner in partners:
    #                             monthentry = partner.journal.monthentries.current().first()
    #                             if monthentry:
    #                                 partner.focus = format_html_join('', '{0} [{1}]<br>',
    #                                                                  ((outcome, outcome.get_status_display()) for
    #                                                                   outcome in monthentry.outcomes))
    #     return self.render(request, template='community/tribe.html', context=context)
    #
    # @route(r'^join/$')
    # def join(self, request):
    #     context = self.get_context(request)
    #     context['mentors'] = set([duo.mentor for duo in Duo.objects.open()])
    #     return self.render(request, template='community/join.html', context=context)


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
                print('{} has duo {}'.format(user, duo))
                context['duo'] = duo
                context['scope'] = Day()
            else:
                print('{} has no duo {}'.format(user, duo))
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
