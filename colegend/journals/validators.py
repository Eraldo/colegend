import datetime
from django.core.exceptions import ValidationError

__author__ = 'eraldo'


def validate_present_or_past(date):
    if date > datetime.date.today():
        raise ValidationError('Date needs to be today or in the past.')
