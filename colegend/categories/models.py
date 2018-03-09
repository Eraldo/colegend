from django.db import models
from colegend.core.models import AutoUrlsMixin
from django.utils.translation import ugettext_lazy as _


class Category(AutoUrlsMixin, models.Model):
    order = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = _('categories')
        ordering = ['-order']

    def __str__(self):
        return '{}: {}'.format(self.order, self.name)
