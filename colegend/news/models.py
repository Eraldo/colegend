from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page

from colegend.categories.models import Category
from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase


def get_current_date():
    return timezone.now()


class News(TimeStampedBase):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    date = models.DateTimeField(
        _('date'),
        default=get_current_date
    )
    image_url = models.URLField(
        _('image url'),
        max_length=1000,
        blank=True
    )
    video_url = models.URLField(
        _('video url'),
        max_length=1000,
        blank=True
    )
    description = models.TextField(
        _('short description'),
        blank=True
    )
    content = MarkdownField()
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    class Meta:
        default_related_name = 'news'
        ordering = ['-date']
        verbose_name_plural = _('news')

    def __str__(self):
        return self.name


class NewsPage(Page):
    template = 'news/base.html'

    # def serve(self, request, *args, **kwargs):
    #     return redirect(self.get_first_child().url)

    parent_page_types = ['cms.RootPage']
    subpage_types = []
