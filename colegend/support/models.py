from django.template.defaultfilters import slugify
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS
from colegend.cms.models import UniquePageMixin
from colegend.core.templatetags.core_tags import card, link, icon


class SupportPage(UniquePageMixin, Page):
    template = 'support/index.html'

    class Meta:
        verbose_name = _('Support')

    parent_page_types = ['home.HomePage']

    # subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        subpages = self.get_children().live()
        context['cards'] = [
            link(
                card(
                    format_html(
                        '{icon}<br>{content}',
                        icon=icon(slugify(page), classes='fa-3x'),
                        content=page,
                    ), classes='text-center'
                ),
                url=page.url,
                unstyled=True
            )
            for page in subpages
            ]
        return context


class FAQPage(UniquePageMixin, Page):
    template = 'support/faq.html'

    class Meta:
        verbose_name = _('FAQ')

    parent_page_types = ['support.SupportPage']
    # subpage_types = []


class DocumentationIndexPage(UniquePageMixin, Page):
    template = 'support/documentation/index.html'

    @property
    def pages(self):
        pages = self.get_children().live().in_menu()
        # pages = DocumentationPage.objects.children_of(self).live().in_menu()
        return pages

    class Meta:
        verbose_name = _('Documentation index')

    parent_page_types = ['support.SupportPage']
    subpage_types = ['support.DocumentationPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        pages = self.pages
        context['pages'] = pages
        context['cards'] = [
            link(
                card(
                    format_html(
                        '{icon}<br>{content}',
                        icon=icon(slugify(page), classes='fa-3x'),
                        content=page,
                    ), classes='text-center'
                ),
                url=page.url,
                unstyled=True
            )
            for page in pages
            ]
        return context


class DocumentationPage(Page):
    template = 'support/documentation/page.html'

    content = StreamField(
        BASE_BLOCKS,
        blank=True,
    )

    class Meta:
        verbose_name = _('Documentation')
        verbose_name_plural = _('Documentation')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['support.DocumentationIndexPage', 'support.DocumentationPage']
    subpage_types = ['support.DocumentationPage']

    def get_documentation_root(self):
        # Find closest ancestor which is a documentation index
        return self.get_ancestors().type(DocumentationIndexPage).last()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        index = self.get_documentation_root()
        context['content'] = self.content
        context['index'] = index
        return context
