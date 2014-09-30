from django.conf import settings
from django.db import models

__author__ = 'eraldo'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Module(models.Model):
    """
    A course module with some content to learn about and practise.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    category = models.ForeignKey(Category)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
