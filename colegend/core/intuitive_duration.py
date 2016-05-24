import datetime
import re
from django.core.exceptions import ValidationError

__author__ = 'eraldo'

intuitive_duration_format = "__years __months __weeks __days __hours __minutes __seconds"


def parse_intuitive_duration(intuitive_string):
    """
    Takes an intuitive duration string returns a duration object.
    Examples for valid input:
        '1w 6d 20h 15m': one week, six days, twenty hours, 15 minutes
        '1h'           : one hour
    :param intuitive_string: a python string
    :return: timedelta or input value
    """
    intuitive_duration_regex = re.compile(
        r'^{years}(\s+)?{months}(\s+)?{weeks}(\s+)?{days}(\s+)?{hours}(\s+)?{minutes}(\s+)?{seconds}$'.format(
            years=r'((?P<years>\d+?)\s?(?:Y|year(?:s)?))?',
            months=r'((?P<months>\d+?)\s?(?:M|month(?:s)?))?',
            weeks=r'((?P<weeks>\d+?)\s?(?:w|week(?:s)?))?',
            days=r'((?P<days>\d+?)\s?(?:d|day(?:s)?))?',
            hours=r'((?P<hours>\d+?)\s?(?:h|hour(?:s)?))?',
            minutes=r'((?P<minutes>\d+?)\s?(?:m|minute(?:s)?))?',
            seconds=r'((?P<seconds>\d+?)\s?(?:s|second(?:s)?))?',
        )
    )

    # Only accept strings for further processing.
    if not isinstance(intuitive_string, str):
        raise ValidationError("Invalid input for a intuitive duration")

    # Remove spaces from start and end.
    string = intuitive_string.strip()

    parts = intuitive_duration_regex.match(string)

    # Check if the pattern matches.
    if not parts:
        raise ValidationError("Invalid input for an intuitive duration. Format: {}".format(intuitive_duration_format))

    # Separate the string into time parameters. (hours, minutes, etc)
    parts = parts.groupdict()
    time_parameters = {}
    for (name, parameter) in parts.items():
        if parameter:
            time_parameters[name] = int(parameter)

    # Convert the weeks and months to days
    if 'years' in time_parameters:
        time_parameters['days'] = time_parameters.get('days', 0) + time_parameters['years'] * 365
        del time_parameters['years']
    if 'months' in time_parameters:
        time_parameters['days'] = time_parameters.get('days', 0) + time_parameters['months'] * 30
        del time_parameters['months']

    return datetime.timedelta(**time_parameters)


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
        ValidationError("Invalid input for an intuitive duration. Format: {}".format(intuitive_duration_format))

    minutes, seconds = divmod(timedelta.seconds, 60)
    hours, minutes = divmod(minutes, 60)

    years, days = divmod(timedelta.days, 365)
    months, days = divmod(days, 30)
    weeks, days = divmod(days, 30)

    template = '{years}{months}{weeks}{days}{hours}{minutes}{seconds}'

    intuitive_string = template.format(
        years='{}Y '.format(years) if years else '',
        months='{}M '.format(months) if months else '',
        weeks='{}w '.format(weeks) if weeks else '',
        days='{}d '.format(days) if days else '',
        hours='{}h '.format(hours) if hours else '',
        minutes='{}m '.format(minutes) if minutes else '',
        seconds='{}s '.format(seconds) if seconds else '',
    ).rstrip()

    return intuitive_string
