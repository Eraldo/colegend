from django.db import models

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.templatetags.wagtailcore_tags import slugurl

from colegend.cms.models import UniquePageMixin
from colegend.core.templatetags.core_tags import link

from django.utils.translation import ugettext_lazy as _


class HomePage(UniquePageMixin, Page):
    template = 'home/index.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full"),
    ]

    def serve(self, request, *args, **kwargs):
        user = request.user
        # Redirect anonymous users to the about page.
        if not user.is_authenticated():
            return redirect(slugurl(context={'request': request}, slug='about'))
        # Redirect if prologue is not completed.
        if not user.has_checkpoint('prologue'):
            return redirect("story:prologue")
        return super().serve(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['next_step'] = self.get_next_step(request.user)
        return context

    def get_next_step(self, user):
        # Has the user written his journal entry?
        today = timezone.now().date()
        dayentry = user.journal.dayentries.filter(date=today)
        if not dayentry:
            return link(_('Create a journal entry'), reverse('dayentries:create'))

    def __str__(self):
        return self.title


class JoinPage(Page):
    template = 'home/join.html'
