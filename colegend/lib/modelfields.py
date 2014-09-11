from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _
from lib.validators import PhoneValidator

__author__ = 'eraldo'


class PhoneField(CharField):
    description = _("Phone number in the format: +XXXXXXXXXXXXXXX (up to %(max_length)s numbers)")

    default_validators = [PhoneValidator()]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 16
        kwargs['min_length'] = 10
        super(PhoneField, self).__init__(*args, **kwargs)
