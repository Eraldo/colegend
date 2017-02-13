from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import format_html_join, format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.wagtailroutablepage.models import route, RoutablePageMixin
from wagtail.wagtailcore.models import Page


class CommunityPage(RoutablePageMixin, Page):
    template = 'community/index.html'

    class Meta:
        verbose_name = _('community')
        verbose_name_plural = _('communities')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['tribes'] = Tribe.objects.all()
        context['clans'] = Clan.objects.all()
        context['duos'] = Duo.objects.all()
        return context

    def render(self, request, template=None, context=None):
        request.is_preview = getattr(request, 'is_preview', False)
        return TemplateResponse(
            request,
            template or self.get_template(request),
            context or self.get_context(request)
        )

    @route(r'^$')
    def index(self, request):
        return self.render(request)

    @route(r'^duo/$')
    def duo(self, request):
        context = self.get_context(request)
        user = request.user
        if user.is_authenticated():
            duo = user.duo
            if duo:
                partner = duo.members.exclude(id=user.id).first()
                if partner:
                    context['partner'] = partner
                    dayentry = partner.journal.dayentries.current().first()
                    if dayentry:
                        partner.focus = format_html_join('', '{0} [{1}]<br>', ((outcome, outcome.get_status_display()) for outcome in dayentry.outcomes))
            context['duo'] = user.duo
        return self.render(request, template='community/duo.html', context=context)

    @route(r'^clan/$')
    def clan(self, request):
        context = self.get_context(request)
        user = request.user
        if user.is_authenticated():
            duo = user.duo
            if duo:
                clan = duo.clan
                if clan:
                    context['clan'] = clan
                    partners = clan.members.exclude(id=user.id)
                    if partners:
                        context['partners'] = partners
                        for partner in partners:
                            weekentry = partner.journal.weekentries.current().first()
                            if weekentry:
                                partner.focus = format_html_join('', '{0} [{1}]<br>',
                                                                 ((outcome, outcome.get_status_display()) for outcome in
                                                                  weekentry.outcomes))
        return self.render(request, template='community/clan.html', context=context)

    @route(r'^tribe/$')
    def tribe(self, request):
        context = self.get_context(request)
        user = request.user
        if user.is_authenticated():
            duo = user.duo
            if duo:
                clan = duo.clan
                if clan:
                    tribe = clan.tribe
                    if tribe:
                        context['tribe'] = tribe
                        partners = tribe.members.exclude(id=user.id)
                        if partners:
                            context['partners'] = partners
                            for partner in partners:
                                monthentry = partner.journal.monthentries.current().first()
                                if monthentry:
                                    partner.focus = format_html_join('', '{0} [{1}]<br>',
                                                                     ((outcome, outcome.get_status_display()) for
                                                                      outcome in monthentry.outcomes))
        return self.render(request, template='community/tribe.html', context=context)

    @route(r'^join/$')
    def join(self, request):
        context = self.get_context(request)
        context['mentors'] = set([duo.mentor for duo in Duo.objects.open()])
        return self.render(request, template='community/join.html', context=context)


class TribeQuerySet(models.QuerySet):
    pass


class Tribe(models.Model):
    mentor = models.OneToOneField(
        verbose_name=_('mentor'),
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={'groups__name': 'Mentors'},
        related_name='tribe',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new tribe')
    )

    @property
    def members(self):
        return get_user_model().objects.filter(duo__clan__tribe=self.pk)

    objects = TribeQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'tribes'


class Clan(models.Model):
    tribe = models.ForeignKey(
        verbose_name=_('tribe'),
        to=Tribe,
        related_name='clans',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new clan'),
    )

    @property
    def mentor(self):
        return self.tribe.mentor

    @property
    def members(self):
        return get_user_model().objects.filter(duo__clan=self.pk)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'clans'


class DuoQuerySet(models.QuerySet):
    def open(self):
        return self.annotate(member_count=Count('members')).filter(member_count__lte=1).order_by('-member_count')


class Duo(models.Model):
    clan = models.ForeignKey(
        verbose_name=_('clan'),
        to=Clan,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new duo')
    )

    @property
    def mentor(self):
        return self.clan.mentor

    objects = DuoQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'duos'
