from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase

STANDARD = 'standard'
CORE = 'core'
CIRCLE = 'circle'

KIND_TYPES = (
    (STANDARD, _('standard')),
    (CORE, _('core')),
    (CIRCLE, _('circle')),
)


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

    def circles(self):
        """
        Filter only roles that act as circles.
        :return: Filtered queryset.
        """
        return self.filter(kind=CIRCLE)

    def cores(self):
        """
        Filter only core roles.
        :return: Filtered queryset.
        """
        return self.filter(kind=CORE)


class Role(TimeStampedBase):
    kind = models.CharField(
        max_length=25,
        choices=KIND_TYPES,
        default=STANDARD
    )
    circle = models.ForeignKey(
        to='self',
        null=True, blank=True,
        on_delete=models.CASCADE,
        limit_choices_to={'kind': CIRCLE},
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
    purpose = MarkdownField(
        _('purpose'),
    )
    strategy = MarkdownField(
        _('strategy'),
        blank=True
    )
    powers = MarkdownField(
        _('powers'),
        blank=True
    )
    services = MarkdownField(
        _('services'),
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
    description = models.TextField(
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
