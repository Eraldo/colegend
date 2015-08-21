import datetime
from lib.intuitive_duration import intuitive_duration_string
from django import template

__author__ = 'eraldo'

register = template.Library()


@register.filter(name='intuitive_duration')
def get_intuitive_duration(value):
    if not value or not isinstance(value, datetime.timedelta):
        return

    return intuitive_duration_string(value)
