import pprint

from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def atom(context, atom=None, **kwargs):
    atom = atom or context.get('atom')
    name = atom.get('name')
    template = atom.get('template')
    atom_context = atom.get('context')
    context = {
        'name': name,
        'template': template,
        'context': pprint.pformat(atom_context),
    }
    context.update(kwargs)
    atom_meta = render_to_string('styleguide/atoms/meta.html', context=context)
    atom_output = render_to_string(template, context=atom_context)
    return atom_meta + atom_output
