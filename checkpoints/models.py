from django.db import models
from django.utils.translation import ugettext_lazy as _


class Checkpoint(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        default_related_name = 'checkpoints'

    def __str__(self):
        return self.name
