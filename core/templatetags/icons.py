from django import template

from core.utils.icons import get_icon

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag
def icon(name, large=False, fixed=False, spin=False, pulse=False, li=False,
         rotate=False, border=False, color=False, classes=None):
    return get_icon(name, large=large, fixed=fixed, spin=spin, pulse=pulse, li=li, rotate=rotate, border=border,
                    color=color, classes=classes)
