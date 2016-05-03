import pprint

from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def atom(context, **kwargs):
    name = context.get('name')
    data = context.get('data')
    context = {
        'name': name,
        'template': data.get('template'),
        'context': pprint.pformat(data.get('context')),
    }
    context.update(kwargs)
    template = 'styleguide/atoms/meta.html'
    atom_meta = render_to_string(template, context=context)
    atom_output = render_to_string(data.get('template'), context=data.get('context'))
    return atom_meta + atom_output
