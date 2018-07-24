from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from ordered_model.models import OrderedModel
from phonenumber_field.modelfields import PhoneNumberField

from colegend.core.fields import MarkdownField
from colegend.core.models import TimeStampedBase
from django.utils.translation import ugettext_lazy as _

from colegend.users.models import User


class Tag(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']
        default_related_name = 'tags'

    def __str__(self):
        return self.name


class Status(OrderedModel):
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )

    class Meta(OrderedModel.Meta):
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
        default_related_name = 'statuses'

    def __str__(self):
        return self.name


def get_default_status():
    return Status.objects.get_or_create(name='New')[0].pk


class Lead(TimeStampedBase):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.PROTECT,
        default=get_default_status
    )
    email = models.EmailField(
        _('email address'),
        blank=True
    )
    phone = PhoneNumberField(
        verbose_name=_('phone'),
        blank=True,
        help_text=_('International format: e.g "+4917612345678"')
    )
    url = models.URLField(
        _('url'),
        max_length=1000,
        blank=True
    )
    country = CountryField(
        verbose_name=_('country'),
        blank=True
    )
    address = models.TextField(
        verbose_name=_('address'),
        blank=True
    )
    gender = models.CharField(
        verbose_name=_('gender'),
        max_length=1,
        choices=User.GENDER_CHOICES,
        default=User.NEUTRAL
    )
    birthday = models.DateField(
        verbose_name=_('birthday'),
        null=True, blank=True,
    )
    history = MarkdownField(
        verbose_name=_('history'),
        blank=True
    )
    notes = MarkdownField(
        verbose_name=_('notes'),
        blank=True
    )
    tags = models.ManyToManyField(
        to=Tag,
        blank=True
    )
    first_contact = models.DateField(
        _('first contact'),
        blank=True,
        null=True,
        help_text=_('When was this lead first contacted?'),
    )
    last_contact = models.DateField(
        _('last contact'),
        blank=True,
        null=True,
        help_text=_('When was this lead last contacted?'),
    )
    next_contact = models.DateField(
        _('next contact'),
        blank=True,
        null=True,
        help_text=_('When will this lead be contacted next?'),
    )
    creator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    @property
    def contact(self):
        return self.email or self.url or self.phone

    class Meta:
        default_related_name = 'leads'
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")
        ordering = ['created']

    def __str__(self):
        return self.name
