from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

from colegend.cms.blocks import BASE_BLOCKS


class EventsPage(Page):
    template = 'pages/content.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('content'),
    )

    class Meta:
        verbose_name = _('Content')
