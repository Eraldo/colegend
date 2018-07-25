from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index

from colegend.categories.models import Category
from colegend.cms.blocks import BASE_BLOCKS
from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase


def get_current_date():
    return timezone.now()


class Event(TimeStampedBase):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
    )
    start = models.DateTimeField(
        verbose_name=_('start'),
        default=get_current_date
    )
    end = models.DateTimeField(
        verbose_name=_('end'),
        null=True, blank=True
    )
    location = models.CharField(
        verbose_name=_('location'),
        max_length=255,
        blank=True
    )
    image_url = models.URLField(
        verbose_name=_('image url'),
        max_length=1000,
        blank=True
    )
    video_url = models.URLField(
        verbose_name=_('video url'),
        max_length=1000,
        blank=True
    )
    description = models.TextField(
        verbose_name=_('short description'),
        blank=True
    )
    content = MarkdownField(
        verbose_name=_('content'),
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )

    class Meta:
        default_related_name = 'events'
        ordering = ['-start']

    def __str__(self):
        return self.name


class EventsPage(Page):
    template = 'events/calendar.html'

    content = StreamField(BASE_BLOCKS, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    class Meta:
        verbose_name = _('Events')

    parent_page_types = ['cms.RootPage']
    # subpage_types = []
