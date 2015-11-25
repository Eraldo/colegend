from django.db import models
from django.utils.translation import ugettext as _
from core.models import AutoOwnedBase, TimeStampedBase


class Connected(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the 'connected' path of the user.
    """
    guidelines = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)
    guide = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('connected path')
        verbose_name_plural = _('connected path')

    def __str__(self):
        return _("Connected path of {}").format(self.owner)
