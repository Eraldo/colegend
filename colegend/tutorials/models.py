from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase


class Tutorial(TimeStampedBase):
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    video_url = models.URLField(
        _('video url'),
        blank=True
    )
    content = MarkdownField()

    class Meta:
        default_related_name = 'tutorials'
        ordering = ['name']

    def __str__(self):
        return self.name
