from django import template
from lib.views import get_icon

register = template.Library()

__author__ = 'eraldo'


@register.simple_tag
def icon(icon_name):
    return get_icon(icon_name)
