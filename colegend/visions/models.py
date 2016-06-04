from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet


class VisionQuerySet(OwnedQuerySet):
    pass


class Vision(AutoUrlsMixin, OwnedBase):
    """
    A django model representing a user's vision.
    """
    name = models.CharField(
        _('name'), 
        max_length=255,
    )

    objects = VisionQuerySet.as_manager()

    class Meta:
        verbose_name = _('vision')
        verbose_name_plural = _('visions')
        default_related_name = 'visions'

    def __str__(self):
        return self.name
