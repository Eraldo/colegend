import datetime
import re
from django.core.exceptions import ValidationError

__author__ = 'eraldo'

intuitive_duration_format = "A number followed by the scope (seconds|hours|days|weeks|months). Example: 3d or 2.5 hours"


def parse_intuitive_duration(intuitive_string):
    """
    Takes an intuitive duration string returns a duration object.
    Examples for valid input:
        '15m': 15 minutes
        '20h': Twenty hours
        '6d': Six days
        '1w': One week
    :param intuitive_string: a python string
    :return: timedelta or input value
    """
    intuitive_duration_regex = re.compile(
        r'^{amount}(\s+)?({minutes}|{hours}|{days}|{weeks}|{months})$'.format(
            amount=r'(?P<amount>\d+(\.\d+)?|(\d+)?\.\d+)',
            minutes=r'(?P<minutes>m|minute(s)?)',
            hours=r'(?P<hours>h|hour(s)?)',
            days=r'(?P<days>d|day(s)?)',
            weeks=r'(?P<weeks>w|week(s)?)',
            months=r'(?P<months>M|month(s)?)',
        )
    )

    # Only accept strings for further processing.
    if not isinstance(intuitive_string, str):
        raise ValidationError("Invalid input for a duration")

    # Remove spaces from start and end.
    string = intuitive_string.strip()

    parts = intuitive_duration_regex.match(string)

    # Check if the pattern matches.
    if not parts:
        raise ValidationError("Invalid input for a duration. Format: {}".format(intuitive_duration_format))

    # Separate the string into time parameters. (amount, hours, minutes, etc)
    parts = parts.groupdict()
    # Clean empty groups
    parts = {k: v for k, v in parts.items() if v}

    amount = float(parts.pop('amount'))
    scope = parts.popitem()[0]

    if scope == 'months':
        amount *= 30
        scope = 'days'

    time_parameters = {scope: amount}
    duration = datetime.timedelta(**time_parameters)
    return duration


def intuitive_duration_string(timedelta):
    """
    Takes a time duration and converts it to a string representation.
    The string intervals for representation:
        years, months, weeks, days, hours, minutes and seconds.
    Alternative represention with short characters:
        Y, M, w, d, h, m and s
    Example:
        '1w 6d 20h 15m': one week, six days, twenty hours, 15 minutes
        '1h'           : one hour
    :param timedelta: python timedelta object
    :return: a string 'intuitively' representing the duration
    """
    if not isinstance(timedelta, datetime.timedelta):
        raise ValidationError("Invalid input for an intuitive duration. Format: {}".format(intuitive_duration_format))

    if not timedelta.days:
        seconds = timedelta.seconds
        minutes = seconds / 60
        hours = minutes / 60
        if hours >= 1:
            symbol = 'h'
            amount = hours
        else:
            symbol = 'm'
            amount = minutes
    else:
        days = timedelta.days
        weeks = days / 7
        months = days / 30
        if months >= 1:
            symbol = 'M'
            amount = months
        elif weeks >= 1:
            symbol = 'w'
            amount = weeks
        else:
            symbol = 'd'
            amount = days + timedelta.seconds / 60 / 60 / 24

    return '{0:g}{1}'.format(round(amount, 1), symbol)
