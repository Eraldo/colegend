from django.db import models
from django.utils.translation import ugettext as _
from core.models import AutoOwnedBase, TimeStampedBase


class Conscious(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the 'conscious' path of the user.
    """

    # stage = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('conscious path')
        verbose_name_plural = _('conscious path')

    def __str__(self):
        return _("Conscious path of {}").format(self.owner)
