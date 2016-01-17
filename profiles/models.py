from easy_thumbnails.fields import ThumbnailerImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import AutoOwnedBase, TimeStampedBase


class Profile(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the user as a whole complete with:
    + general profile information
    + hero profile
    + demon profile
    """

    biography = models.TextField(blank=True)

    def __str__(self):
        return "{}' profile".format(self.owner)

    def get_absolute_url(self):
        return reverse('profiles:detail', kwargs={'owner': self.owner.username})
