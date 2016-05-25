from django import template
from django.core.exceptions import ValidationError

from colegend.core.intuitive_duration import intuitive_duration_string

register = template.Library()


@register.filter
def intuitive_duration(value):
    try:
        return intuitive_duration_string(value)
    except ValidationError:
        return ''
