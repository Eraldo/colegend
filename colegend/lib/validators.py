import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

__author__ = 'eraldo'


class PhoneValidator(RegexValidator):
    regex = r'^\+1?\d{9,15}$'
    message = "Format Example: +1234567890\n('+' followed by 9-15 digits)"
    code = "invalid_phone_number"


def validate_date_in_past(date):
    if date and date >= datetime.date.today():
        raise ValidationError('Date needs to be in the past.')


def validate_date_today_or_in_past(date):
    if date and date > timezone.now().date():
        raise ValidationError('Needs to be today or in the past.')


def validate_date_within_days(date, days):
    today = timezone.now().date()
    margin = timezone.timedelta(days=days)
    if date and not today - margin <= date <= today + margin:
        raise ValidationError('Needs to be within {} days.'.format(days))


def validate_date_within_one_week(date):
    validate_date_within_days(date, 7)


def validate_datetime_in_past(time):
    if time and time > timezone.now():
        raise ValidationError('Needs to be now or in the past.')
