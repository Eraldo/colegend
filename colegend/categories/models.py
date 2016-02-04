from django.db import models
from orderable.models import Orderable

from colegend.core.models import AutoUrlsMixin


class Category(AutoUrlsMixin, models.Model):
    order = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['-order']

    def __str__(self):
        return '{}: {}'.format(self.order, self.name)
