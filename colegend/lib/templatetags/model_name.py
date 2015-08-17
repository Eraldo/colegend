from django import template

__author__ = 'eraldo'

register = template.Library()


@register.filter
def model_name(value):
    return value.__class__.__name__


@register.filter
def verbose_name(value):
    return  value.__class__._meta.verbose_name.title()


@register.filter
def verbose_name_plural(value):
    return  value.__class__._meta.verbose_name_plural.title()
