from django.contrib import messages
from django.core.mail import EmailMessage
from django.db import models
from django.db.models import Count
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page

from colegend.journals.scopes import Day, Week, Month


class CommunityPage(Page):
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
            duo.join(user)
            messages.success(request, 'You created a new duo: "{0}"'.format(duo.name))
            return redirect(self.url)

        return TemplateResponse(
            request,
            'community/duo_create.html',
            context,
        )

    @route(r'^join/$')
    def join(self, request):
        user = request.user
        id = request.POST.get('id')
        if not id or not user.is_authenticated:
            return redirect(self.url)

        # Getting duo
        try:
            duo = Duo.objects.get(id=int(id))
        except Duo.DoesNotExist:
            raise Exception('Duo with id "{}" does not exist.'.format(id))

        # Adding user to duo
        try:
            duo.join(user)
            messages.success(request, 'You have been added to duo "{0}"'.format(duo))
        except Exception as exception:
            messages.error(request, exception)
        return redirect(self.url)

    @route(r'^quit/$')
    def quit(self, request):
        user = request.user
        action = request.POST.get('action')

        if action == 'confirm' and user.is_authenticated:
            duo = user.duo
            try:
                duo.quit(user)
                messages.success(request, 'You left duo: "{0}"'.format(duo))
            except Exception as exception:
                messages.error(request, exception)
            return redirect(self.url)
        elif action == 'cancel':
            return redirect(self.url)
        return TemplateResponse(
            request,
            'community/duo_quit.html',
            {'duo': user.duo},
        )


class ClanPage(RoutablePageMixin, Page):
    template = 'community/clan.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        user = request.user
        if user.is_authenticated:
            clan = user.clan
            if clan:
                context['clan'] = clan
                context['scope'] = Week()
        return context

    def __str__(self):
        return self.title

    @route(r'^$')
    def index(self, request):
        user = request.user
        if not user.clan:
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
        context['clans'] = Clan.objects.all()
        return TemplateResponse(
            request,
            'community/clan_list.html',
            context,
        )

    @route(r'^create/$')
    def create(self, request):
        context = self.get_context(request)
        user = request.user
        if not user.is_authenticated or user.clan:
            return redirect(self.url)

        from colegend.community.forms import ClanForm
        if request.POST:
            form = ClanForm(request.POST)
        else:
            form = ClanForm()
        context['form'] = form

        if form.is_valid():
            clan = form.save()
            clan.join(user)
            messages.success(request, 'You created a new clan: "{0}"'.format(clan.name))
            return redirect(self.url)

        return TemplateResponse(
            request,
            'community/clan_create.html',
            context,
        )

    @route(r'^join/$')
    def join(self, request):
        user = request.user
        id = request.POST.get('id')
        if not id or not user.is_authenticated:
            return redirect(self.url)

        # Getting clan
        try:
            clan = Clan.objects.get(id=int(id))
        except Clan.DoesNotExist:
            raise Exception('Clan with id "{}" does not exist.'.format(id))

        # Adding user to clan
        try:
            clan.join(user)
            messages.success(request, 'You have been added to clan "{0}"'.format(clan))
        except Exception as exception:
            messages.error(request, exception)
        return redirect(self.url)

    @route(r'^quit/$')
    def quit(self, request):
        user = request.user
        action = request.POST.get('action')

        if action == 'confirm' and user.is_authenticated:
            clan = user.clan
            try:
                clan.quit(user)
                messages.success(request, 'You left clan: "{0}"'.format(clan))
            except Exception as exception:
                messages.error(request, exception)
            return redirect(self.url)
        elif action == 'cancel':
            return redirect(self.url)
        return TemplateResponse(
            request,
            'community/clan_quit.html',
            {'clan': user.clan},
        )


class TribePage(RoutablePageMixin, Page):
    template = 'community/tribe.html'

    parent_page_types = ['CommunityPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        user = request.user
        if user.is_authenticated:
            tribe = user.tribe
            if tribe:
                context['tribe'] = tribe
                context['scope'] = Month()
        return context

    def __str__(self):
        return self.title

    @route(r'^$')
    def index(self, request):
        user = request.user
        if not user.tribe:
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
        context['tribes'] = Tribe.objects.all()
        return TemplateResponse(
            request,
            'community/tribe_list.html',
            context,
        )

    @route(r'^create/$')
    def create(self, request):
        context = self.get_context(request)
        user = request.user
        if not user.is_authenticated or user.tribe:
            return redirect(self.url)

        from colegend.community.forms import TribeForm
        if request.POST:
            form = TribeForm(request.POST)
        else:
            form = TribeForm()
        context['form'] = form

        if form.is_valid():
            tribe = form.save()
            tribe.join(user)
            messages.success(request, 'You created a new tribe: "{0}"'.format(tribe.name))
            return redirect(self.url)

        return TemplateResponse(
            request,
            'community/tribe_create.html',
            context,
        )

    @route(r'^join/$')
    def join(self, request):
        user = request.user
        id = request.POST.get('id')
        if not id or not user.is_authenticated:
            return redirect(self.url)

        # Getting tribe
        try:
            tribe = Tribe.objects.get(id=int(id))
        except Tribe.DoesNotExist:
            raise Exception('Tribe with id "{}" does not exist.'.format(id))

        # Adding user to tribe
        try:
            tribe.join(user)
            messages.success(request, 'You have been added to tribe "{0}"'.format(tribe))
        except Exception as exception:
            messages.error(request, exception)
        return redirect(self.url)

    @route(r'^quit/$')
    def quit(self, request):
        user = request.user
        action = request.POST.get('action')

        if action == 'confirm' and user.is_authenticated:
            tribe = user.tribe
            try:
                tribe.quit(user)
                messages.success(request, 'You left tribe: "{0}"'.format(tribe))
            except Exception as exception:
                messages.error(request, exception)
            return redirect(self.url)
        elif action == 'cancel':
            return redirect(self.url)
        return TemplateResponse(
            request,
            'community/tribe_quit.html',
            {'tribe': user.tribe},
        )


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

    notes = models.TextField(
        verbose_name=_("notes"),
        blank=True
    )

    objects = TribeQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'tribes'

    @property
    def is_full(self):
        return self.members.count() >= 16

    @property
    def is_open(self):
        return not self.is_full

    def join(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to join "{0}".'.format(self))
        if self.is_full:
            raise Exception('Tribe "{tribe}" is already full.'.format(tribe=self))
        if user.tribe:
            raise Exception('Please quit Tribe "{old}" before joining Tribe "{new}".'.format(old=user.tribe, new=self))
        self.members.add(user)

    def quit(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to quit "{0}".'.format(self))
        if not user.tribe:
            raise Exception('Nothing to quit.')
        self.members.remove(user)

        # Deleting tribe if it is empty
        if not self.members.exists():
            self.delete()

    def notify_partners(self, user, subject, message):
        if not user in self.members.all():
            raise Exception('User "{user}" is not in Tribe "{tribe}"'.format(user=user, duo=self))
        partners = self.members.exclude(id=user.id)
        if partners:
            emails = [partner.email for partner in partners]
            email = EmailMessage(subject=subject, body=message, to=emails, reply_to=[user.email])
            email.send()


class Clan(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new clan'),
    )

    notes = models.TextField(
        verbose_name=_("notes"),
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'clans'

    @property
    def is_full(self):
        return self.members.count() >= 4

    @property
    def is_open(self):
        return not self.is_full

    def join(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to join "{0}".'.format(self))
        if self.is_full:
            raise Exception('Clan "{clan}" is already full.'.format(clan=self))
        if user.clan:
            raise Exception('Please quit Clan "{old}" before joining Clan "{new}".'.format(old=user.clan, new=self))
        self.members.add(user)

    def quit(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to quit "{0}".'.format(self))
        if not user.clan:
            raise Exception('Nothing to quit.')
        self.members.remove(user)

        # Deleting clan if it is empty
        if not self.members.exists():
            self.delete()

    def notify_partners(self, user, subject, message):
        if not user in self.members.all():
            raise Exception('User "{user}" is not in Clan "{clan}"'.format(user=user, duo=self))
        partners = self.members.exclude(id=user.id)
        if partners:
            emails = [partner.email for partner in partners]
            email = EmailMessage(subject=subject, body=message, to=emails, reply_to=[user.email])
            email.send()


class DuoQuerySet(models.QuerySet):
    def open(self):
        return self.annotate(member_count=Count('members')).filter(member_count__lte=1).order_by('-member_count')


class Duo(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        default=_('new duo')
    )

    notes = models.TextField(
        verbose_name=_("notes"),
        blank=True
    )

    objects = DuoQuerySet.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'duos'

    @property
    def is_full(self):
        return self.members.count() >= 2

    @property
    def is_open(self):
        return not self.is_full

    def join(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to join "{0}".'.format(self))
        if self.is_full:
            raise Exception('Duo "{duo}" is already full.'.format(duo=self))
        if user.duo:
            raise Exception('Please quit Duo "{old}" before joining Duo "{new}".'.format(old=user.duo, new=self))
        self.members.add(user)

    def quit(self, user):
        if not user.is_authenticated:
            raise Exception('Please authenticate to quit "{0}".'.format(self))
        if not user.duo:
            raise Exception('Nothing to quit.')
        self.members.remove(user)

        # Checking if duo is empty
        if not self.members.exists():
            self.delete()

    def notify_partners(self, user, subject, message):
        if not user in self.members.all():
            raise Exception('User "{user}" is not in Duo "{duo}"'.format(user=user, duo=self))
        partners = self.members.exclude(id=user.id)
        if partners:
            emails = [partner.email for partner in partners]
            email = EmailMessage(subject=subject, body=message, to=emails, reply_to=[user.email])
            email.send()
