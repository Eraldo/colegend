from django.db import models
from django.utils import timezone
from markitup.fields import MarkupField
from lib.models import OwnedBase, AutoUrlMixin


class NewsBlock(AutoUrlMixin, OwnedBase, models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(default=timezone.now)

    content = MarkupField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
