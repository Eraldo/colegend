from collections import OrderedDict

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from colegend.core.fields import MarkdownField
from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet
from colegend.core.utils.media_paths import UploadToOwnedDirectory


class VisionQuerySet(OwnedQuerySet):
    def scope(self, owner, scope):
        if scope == _('day'):
            return self.get_or_create(owner=owner, scope=Vision.DAY)[0]
        elif scope == _('week'):
            return self.get_or_create(owner=owner, scope=Vision.WEEK)[0]
        elif scope == _('month'):
            return self.get_or_create(owner=owner, scope=Vision.MONTH)[0]
        elif scope == _('quarter'):
            return self.get_or_create(owner=owner, scope=Vision.QUARTER)[0]
        elif scope == _('year'):
            return self.get_or_create(owner=owner, scope=Vision.YEAR)[0]
        else:
            return Vision.objects.none()


class Vision(AutoUrlsMixin, OwnedBase):
    """
    A django model representing a user's vision.
    """
    DAY = 1
    WEEK = 2
    MONTH = 3
    QUARTER = 4
    YEAR = 5
    SCOPE_CHOICES = (
        (DAY, _('day')),
        (WEEK, _('week')),
        (MONTH, _('month')),
        (QUARTER, _('quarter')),
        (YEAR, _('year')),
    )
    SCOPE_MAP = OrderedDict(SCOPE_CHOICES)
    scope = models.PositiveSmallIntegerField(
        _('scope'),
        choices=SCOPE_CHOICES,
        default=DAY,
    )

    image = ThumbnailerImageField(
        verbose_name=_('image'),
        upload_to=UploadToOwnedDirectory('vision', ),
        resize_source=dict(size=(1200, 1200)),
        blank=True
    )

    content = MarkdownField(blank=True)

    objects = VisionQuerySet.as_manager()

    class Meta:
        verbose_name = _('vision')
        verbose_name_plural = _('visions')
        default_related_name = 'visions'
        unique_together = ('owner', 'scope')

    def __str__(self):
        return "{}'s {} vision".format(self.owner, self.get_scope_display())

    @property
    def create_url(self):
        url = '{}create'.format(self.auto_url_prefix)
        return reverse(url, kwargs={'scope': self.get_scope_display()})

    @property
    def detail_url(self):
        url = '{}detail'.format(self.auto_url_prefix)
        return reverse(url, kwargs={'scope': self.get_scope_display()})

    @property
    def update_url(self):
        url = '{}update'.format(self.auto_url_prefix)
        return reverse(url, kwargs={'scope': self.get_scope_display()})

    @property
    def delete_url(self):
        url = '{}delete'.format(self.auto_url_prefix)
        return reverse(url, kwargs={'scope': self.get_scope_display()})
