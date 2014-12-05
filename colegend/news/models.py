from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from markitup.fields import MarkupField
from lib.models import OwnedBase, AutoUrlMixin


class NewsBlock(AutoUrlMixin, OwnedBase, models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(default=timezone.now)
    sticky = models.BooleanField(default=False)

    content = MarkupField(blank=True)

    class Meta:
        ordering = ['-sticky', '-date']

    def __str__(self):
        return self.name
