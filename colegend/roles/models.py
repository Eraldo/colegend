from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoleQuerySet(models.QuerySet):
    def contains_name(self, name):
        """
        Check if the role set has a role with the supplied name.
        :param name: A string. (role name)
        :return: True if the user a role with that name. False otherwise.
        """
        return self.filter(name__iexact=name).exists()

    def contains_names(self, names):
        """
        Check if the role set has roles the supplied names.
        :param names: A list of strings. (role names)
        :return: True if the user has a role with each name. False otherwise.
        """
        # Check for all roles individually
        # TODO: refactor to more efficient method
        for name in names:
            if not self.contains_name(name):
                return False
        return True


class Role(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    nickname = models.CharField(_('nickname'), max_length=255, blank=True)
    item = models.CharField(_('item'), max_length=255, blank=True)
    description = models.TextField(blank=True)

    objects = RoleQuerySet.as_manager()

    class Meta:
        default_related_name = 'roles'

    def __str__(self):
        return '{}{}'.format(
            self.name,
            ' ({})'.format(self.nickname) if self.nickname else '',
        )
