from django.contrib import messages
from django.db import models
from django.db.models import Count
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
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


class DuoPage(RoutablePageMixin, Page):
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

    @route(r'^$')
    def index(self, request):
        user = request.user
        if not user.duo:
            return redirect(self.reverse_subpage('list'))
        context = self.get_context(request)
        return TemplateResponse(
            request,
            self.get_template(request),
            context,
        )

    @route(r'^list/$')
    def list(self, request):
        context = self.get_context(request)
        context['duos'] = Duo.objects.all()
        return TemplateResponse(
            request,
            'community/duo_list.html',
            context,
        )

    @route(r'^create/$')
    def create(self, request):
        context = self.get_context(request)
        user = request.user
        if not user.is_authenticated or user.duo:
            return redirect(self.url)

        from colegend.community.forms import DuoForm
        if request.POST:
            form = DuoForm(request.POST)
        else:
            form = DuoForm()
        context['form'] = form

        if form.is_valid():
            duo = form.save()
            user.duo = duo
            user.save()
            messages.success(request, 'You created a new duo: "{0}"'.format(duo.name))
            return redirect(self.url)

        return TemplateResponse(
            request,
            'community/duo_create.html',
            context,
        )

    @route(r'^join/$')
    def join(self, request):
        id = request.POST.get('id')
        if id:
            # Add user to duo
            user = request.user
            if user.duo:
                messages.error(request, 'You are already in a duo: "{0}"'.format(user.duo))
                return redirect(self.url)
            try:
                duo = Duo.objects.get(id=int(id))
            except Duo.DoesNotExist:
                raise ValueError('Duo with id "{}" does not exist.'.format(id))
            user.duo = duo
            user.save()
            messages.success(request, 'You have been added to duo "{0}"'.format(duo))
        return redirect(self.url)

    @route(r'^quit/$')
    def quit(self, request):
        user = request.user
        action = request.POST.get('action')
        if action == 'confirm':
            if user.is_authenticated and user.duo:
                # Remove user from duo
                duo = user.duo
                user.duo = None
                user.save()
                messages.success(request, 'You left duo: "{0}"'.format(duo))
                if not duo.members.exists():
                    duo.delete()
                    messages.info(request, 'Duo "{0}" has been deleted.'.format(duo))
                return redirect(self.url)
        elif action == 'cancel':
            return redirect(self.url)
        return TemplateResponse(
            request,
            'community/duo_quit.html',
            {'duo': user.duo},
        )


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
