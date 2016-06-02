import datetime
from django import forms
from django.core.exceptions import ValidationError

from colegend.core.intuitive_duration.utils import intuitive_duration_string, parse_intuitive_duration


class IntuitiveDurationFormField(forms.DurationField):

    def prepare_value(self, value):
        if isinstance(value, datetime.timedelta):
            return intuitive_duration_string(value)
        return value

    def to_python(self, value):
        if value in self.empty_values:
            return None
        if isinstance(value, datetime.timedelta):
            return value
        value = parse_intuitive_duration(value)
        if value is None:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value
