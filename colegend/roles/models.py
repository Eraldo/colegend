from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase


class Circle(TimeStampedBase):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )
    purpose = MarkdownField(
        _('purpose'),
    )
    strategy = MarkdownField(
        _('strategy'),
        blank=True
    )
    domains = MarkdownField(
        _('domains'),
        blank=True
    )
    accountabilities = MarkdownField(
        _('accountabilities'),
        blank=True
    )
    policies = MarkdownField(
        _('policies'),
        blank=True
    )
    history = MarkdownField(
        _('history'),
        blank=True
    )
    notes = MarkdownField(
        _('notes'),
        blank=True
    )
    checklists = MarkdownField(
        _('checklists'),
        blank=True
    )
    metrics = MarkdownField(
        _('metrics'),
        blank=True
    )

    # TODO: Adding outcomes

    class Meta:
        default_related_name = 'circles'

    def __str__(self):
        return self.name


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


class Role(TimeStampedBase):
    circle = models.ForeignKey(
        to=Circle,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    nickname = models.CharField(
        _('nickname'),
        max_length=255,
        blank=True
    )
    item = models.CharField(
        _('item'),
        max_length=255,
        blank=True
    )
    icon = ThumbnailerImageField(
        upload_to='roles/icons/',
        blank=True,
        resize_source=dict(size=(100, 100)),
    )
    description = models.TextField(
        blank=True
    )
    metrics = models.TextField(
        blank=True
    )

    objects = RoleQuerySet.as_manager()

    class Meta:
        default_related_name = 'roles'
        ordering = ['name']
        unique_together = ['circle', 'name']

    def __str__(self):
        return '{}{}'.format(
            self.name,
            ' ({})'.format(self.nickname) if self.nickname else '',
        )

    @property
    def display_name(self):
        name = self.nickname or self.name
        return '{}'.format(name)
