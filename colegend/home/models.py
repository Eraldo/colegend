from django.conf import settings
from django.db import models

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.templatetags.wagtailcore_tags import slugurl
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS
from colegend.cms.models import UniquePageMixin
from colegend.core.templatetags.core_tags import link

from django.utils.translation import ugettext_lazy as _

from colegend.office.models import DAY, AgendaPage


class HomePage(Page):
    template = 'home/index.html'

    def serve(self, request, *args, **kwargs):
        return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = ['DashboardPage', 'HabitsPage', 'StatsPage']


class DashboardPage(Page):
    template = 'home/dashboard.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['next_step'] = self.get_next_step(request.user)
        return context

    def get_next_step(self, user):
        today = timezone.localtime(timezone.now()).date()

        # Has the user set his focus?
        focus = user.focuses.filter(scope=DAY, start=today)
        agenda_page = AgendaPage.objects.first()
        if not focus and agenda_page:
            url = agenda_page.url + '?scope=day&date={}'.format(today)
            return link(_('Setting focus'), url)

        # Has the user written his journal entry?
        dayentry = user.journal_entries.filter(scope=DAY, start=today)
        if not dayentry:
            return link(_('Create a journal entry'), '#')

    def __str__(self):
        return self.title


class HabitsPage(Page):
    template = 'home/habits.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []


class StatsPage(Page):
    template = 'home/stats.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []


class JoinPage(Page):
    template = 'home/join.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Join')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['open'] = True
        if settings.ACCOUNT_ALLOW_REGISTRATION:
            context['open'] = True
        return context
