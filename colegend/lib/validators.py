import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

__author__ = 'eraldo'


class PhoneValidator(RegexValidator):
    regex = r'^\+1?\d{9,15}$'
    message = "Format Example: +1234567890\n('+' followed by 9-15 digits)"
    code = "invalid_phone_number"


def validate_in_past(date):
    if date >= datetime.date.today():
        raise ValidationError('Date needs to be in the past.')
