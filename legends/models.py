import os

from django.core.urlresolvers import reverse
from django.db import models

from core.models import AutoOwnedBase, TimeStampedBase


def owner_path(sub_directory=None, attribute='owner'):
    # Returns a function that will generate a user path with an optional sub-directory.
    if sub_directory:
        template = 'user_{{0}}/{}/{{1}}'.format(sub_directory)
    else:
        template = 'user_{0}/{1}'

    def specific_user_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/(?:<sub_directory>/)<filename>
        owner = getattr(instance, attribute)
        return template.format(owner.id, filename)

    return specific_user_path


legend_path = owner_path('legend')


class Legend(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the user as a whole complete with:
    + general profile information
    + hero profile
    + demon profile
    """
    avatar = models.ImageField(upload_to=legend_path, blank=True)

    def __str__(self):
        return "Legend {}".format(self.owner)

    def get_absolute_url(self):
        return reverse('legends:detail', kwargs={'owner': self.owner.username})
