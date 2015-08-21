from django.core.validators import MinLengthValidator
from django.db.models import CharField
from lib.formfields import IntuitiveDurationFormField
from lib.intuitive_duration import parse_intuitive_duration, intuitive_duration_string, intuitive_duration_format
from lib.validators import PhoneValidator
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

__author__ = 'eraldo'


class PhoneField(CharField):
    description = _("Phone number in the format: +XXXXXXXXXXXXXXX (up to %(max_length)s numbers)")

    default_validators = [PhoneValidator(), MinLengthValidator(10)]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 16
        super(PhoneField, self).__init__(*args, **kwargs)


class IntuitiveDurationField(models.DurationField):
    """
    Duration field with intuitive human input and output strings.
    """
    description = _("Duration field with intuitive human input and output strings.")

    default_error_messages = {
        'invalid': _("'%(value)s' value has an invalid format. Format: {}".format(intuitive_duration_format))
    }

    def to_python(self, value):
        if isinstance(value, str):
            try:
                parsed = parse_intuitive_duration(value)
            except ValueError:
                pass
            else:
                return parsed
        else:
            value = super().to_python(value)

        if isinstance(value, datetime.timedelta):
            # remove microseconds
            value = datetime.timedelta(days=value.days, seconds=value.seconds)

        return value

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        raise Exception(intuitive_duration_string(value))
        return '' if value is None else intuitive_duration_string(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': IntuitiveDurationFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
