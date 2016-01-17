from django.contrib.auth.models import Permission
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Role(models.Model):
    name = models.CharField(_('name'), max_length=255)
