from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import AutoOwnedBase, TimeStampedBase
from core.utils.media_paths import UploadToOwnedDirectory


class Legend(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the user as a whole complete with:
    + general profile information
    + hero profile
    + demon profile
    """
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(
        _("name"),
        max_length=255,
        help_text=_("Your full name"))

    # personal and contact data
    MALE = 'M'
    FEMALE = 'F'
    NEUTRAL = 'N'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NEUTRAL, 'Neutral'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(_('occupation(s)'), max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)

    address = models.TextField()

    @property
    def city(self):
        address = self.address
        if address:
            parts = address.splitlines()
            if len(parts) >= 2:
                city = parts[1]
            else:
                city = ''
        return city

    phone = PhoneNumberField(blank=True)

    avatar = ThumbnailerImageField(upload_to=UploadToOwnedDirectory('legend'))

    biography = models.TextField(blank=True)

    @property
    def legend_days(self):
        date_joined = self.owner.date_joined
        now = timezone.now()
        return (now - date_joined).days

    @property
    def chapter(self):
        chapter = 1
        return chapter

    def __str__(self):
        return "Legend {}".format(self.owner)

    def get_absolute_url(self):
        return reverse('legends:detail', kwargs={'owner': self.owner.username})
