from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date_present_or_past(date):
    if date > timezone.now().date():
        raise ValidationError('Date needs to be today or in the past.')


def validate_date_today_tomorrow_or_past(date):
    if date > timezone.now().date() + timezone.timedelta(1):
        raise ValidationError('Date needs to be today, tomorrow or in the past.')
