import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .formfields import IntuitiveDurationFormField
from .utils import parse_intuitive_duration, intuitive_duration_format, intuitive_duration_string


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
        return '' if value is None else intuitive_duration_string(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': IntuitiveDurationFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
