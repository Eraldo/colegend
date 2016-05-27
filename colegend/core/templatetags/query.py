from django import template

register = template.Library()

__author__ = 'eraldo'


@register.simple_tag(takes_context=True)
def querystring(context, *args, **kwargs):
    """
    Update and render the original querystring.

    Positional arguments are keys to be dropped.

    Keyword arguments override existing keys.

    {% querystring 'next' page=pagenum %}
    """
    qdict = context['request'].GET.copy()
    # Remove the value-less ones
    for arg in args:
        qdict.pop(arg, None)
    # Set the valued ones
    # We don't use update, because that won't remove old values
    for key, val in kwargs.items():
        qdict[key] = val
    return qdict.urlencode()
