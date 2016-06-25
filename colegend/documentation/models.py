from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS
from colegend.cms.models import UniquePageMixin


class DocumentationIndexPage(UniquePageMixin, Page):
    template = 'documentation/index.html'

    @property
    def pages(self):
        pages = DocumentationPage.objects.descendant_of(self).live()
        return pages

    class Meta:
        verbose_name = _('Documentation')

    # parent_page_types = ['support.SupportPage']
    subpage_types = ['documentation.DocumentationPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        pages = self.pages
        context['pages'] = pages
        return context


class DocumentationPage(Page):
    template = 'documentation/page.html'

    content = StreamField(
        BASE_BLOCKS,
        blank=True,
    )

    class Meta:
        verbose_name = _('Documentation page')
        verbose_name_plural = _('Documentation pages')

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    parent_page_types = ['documentation.DocumentationIndexPage']
    subpage_types = ['documentation.DocumentationPage']

    def get_documentation_root(self):
        # Find closest ancestor which is a documentation index
        return self.get_ancestors().type(DocumentationPage).last()
