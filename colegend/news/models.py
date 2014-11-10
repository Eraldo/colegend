from django.db import models
from django.utils import timezone
from lib.models import OwnedBase, AutoUrlMixin


class NewsBlock(AutoUrlMixin, OwnedBase, models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name
