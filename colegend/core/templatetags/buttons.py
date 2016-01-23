from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def button(context, name, pattern=None, url=None, kind=None, icon=None, locked=False, id=None):
    kind_dict = {
        'list': 'secondary btn-sm',
        'create': 'secondary btn-sm',
        'detail': 'secondary btn-sm',
        'update': 'secondary btn-sm',
        'delete': 'danger btn-sm',
    }
    if not kind:
        kind = kind_dict.get(name, 'primary')

    if not url and pattern:
        url = reverse(pattern)

    if not icon and name in kind_dict.keys():
        icon = name

    context = {
        'name': name,
        'url': url,
        'kind': kind,
        'icon': icon,
        'locked': locked,
        'id': id,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)
