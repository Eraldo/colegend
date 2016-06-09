from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.html import format_html

from colegend.core.templatetags.core_tags import icon as render_icon

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

    if locked:
        icon = 'locked'
        url = None
        kind += ' disabled'

    if icon:
        content = format_html(
            '{icon} {name}', icon=render_icon(icon, fixed=True), name=name)
    else:
        content = name

    context = {
        'url': url,
        'classes': 'btn btn-{}'.format(kind),
        'content': content,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def contact_button(context, **kwargs):
    context = {
        'name': 'Connect',
        'url': 'mailto:connect@colegend.org',
        'kind': 'secondary btn-sm',
        'icon': 'send',
    }
    context.update(kwargs)
    template = 'widgets/button.html'
    return render_to_string(template, context=context)
