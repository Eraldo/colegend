from django.db import ProgrammingError
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.templatetags.wagtailcore_tags import slugurl
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS

__author__ = 'Eraldo Energy'


class UniquePageMixin(object):
    """
    Mixin for Wagtail pages to make sure only one of this Page exists.
    """

    @classmethod
    def clean_parent_page_models(cls):
        # Only allow a single instance.
        try:
            if cls.objects and cls.objects.exists():
                return []
        except ProgrammingError:  # not migrated yet.
            pass
        return super().clean_parent_page_models()


class RootPage(UniquePageMixin, Page):
    template = 'pages/root.html'

    class Meta:
        verbose_name = _('Root')

    def serve(self, request, *args, **kwargs):
        user = request.user
        # Redirect anonymous users to the about page.
        if not user.is_authenticated():
            return redirect(slugurl(context={'request': request}, slug='about'))
        # Redirect if prologue is not completed.
        # if not user.has_checkpoint('prologue'):
        #     return redirect("story:prologue")
        # Redirecto to first subpage
        return redirect(self.get_first_child().url)


class ContentPage(Page):
    template = 'pages/content.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Content')
