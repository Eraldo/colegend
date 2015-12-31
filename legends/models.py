from django.core.urlresolvers import reverse
from easy_thumbnails.fields import ThumbnailerImageField

from core.models import AutoOwnedBase, TimeStampedBase
from core.utils.media_paths import UploadToOwnedDirectory


class Legend(AutoOwnedBase, TimeStampedBase):
    """
    A django model representing the user as a whole complete with:
    + general profile information
    + hero profile
    + demon profile
    """
    avatar = ThumbnailerImageField(upload_to=UploadToOwnedDirectory('legend'), blank=True)

    def __str__(self):
        return "Legend {}".format(self.owner)

    def get_absolute_url(self):
        return reverse('legends:detail', kwargs={'owner': self.owner.username})
