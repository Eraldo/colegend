from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.db import models


class TimeStampedBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnedBase(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class SingleOwnedBase(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class AutoOwnedBase(models.Model):
    owner = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    class Meta:
        abstract = True
