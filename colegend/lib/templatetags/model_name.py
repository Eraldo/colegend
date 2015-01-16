from django import template

__author__ = 'eraldo'

register = template.Library()


@register.filter
def model_name(value):
    return value.__class__.__name__
