from django.db import models
from django.utils.translation import ugettext_lazy as _


class CheckpointQuerySet(models.QuerySet):
    def contains_name(self, name):
        """
        Check if the checkpoint set has a checkpoint with the supplied name.
        :param name: A string. (checkpoint name)
        :return: True if the user a checkpoint with that name. False otherwise.
        """
        return self.filter(name__iexact=name).exists()

    def contains_names(self, names):
        """
        Check if the checkpoint set has checkpoints the supplied names.
        :param names: A list of strings. (checkpoint names)
        :return: True if the user has a checkpoint with each name. False otherwise.
        """
        # Check for all checkpoints individually
        # TODO: refactor to more efficient method
        for name in names:
            if not self.contains_name(name):
                return False
        return True


class Checkpoint(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        default_related_name = 'checkpoints'

    objects = CheckpointQuerySet.as_manager()

    def __str__(self):
        return self.name
