from django.db import models
from django.utils.translation import ugettext_lazy as _

from colegend.categories.models import Category
from colegend.core.models import OwnedBase, AutoUrlsMixin, OwnedQuerySet


class TagQuerySet(OwnedQuerySet):
    pass


class Tag(AutoUrlsMixin, OwnedBase):
    """
    A django model representing a user's text-tag.
    """
    name = models.CharField(_('name'), max_length=255)

    description = models.TextField(blank=True)

    category = models.ForeignKey(Category, blank=True, null=True)

    objects = TagQuerySet.as_manager()

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        unique_together = ['owner', 'name']
        ordering = ['name']
        default_related_name = 'tags'

    def __str__(self):
        return self.name


class TaggableBase(models.Model):
    """
    Adds a tags relation to the model. *-*
    """
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True
