from django.db import models
from django.utils.translation import ugettext as _
from core.models import AutoOwnedBase, TimeStampedBase


class Continuous(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the 'continuous' path of the user.
    """
    chapter = models.PositiveSmallIntegerField(default=0)
    prologue_country = models.CharField(max_length=255, blank=True)
    prologue = models.BooleanField(default=False)
    leyenda = models.BooleanField(default=False)
    pioneer_journal = models.BooleanField(default=False)
    your_journal = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('continuous path')
        verbose_name_plural = _('continuous path')

    def __str__(self):
        return _("Continuous path of {}").format(self.owner)
