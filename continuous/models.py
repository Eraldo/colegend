from django.db import models
from django.utils.translation import ugettext as _
from core.models import AutoOwnedBase, TimeStampedBase


class Continuous(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the 'continuous' path of the user.
    """
    prologue = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('continuous path')
        verbose_name_plural = _('continuous path')

    def __str__(self):
        return _("Continuous path of {}").format(self.owner)
