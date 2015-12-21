from django import template

from core.utils.icons import get_icon

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag
def icon(name):
    return get_icon(name)
