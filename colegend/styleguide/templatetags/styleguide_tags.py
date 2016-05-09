import pprint

from django import template
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def toc(context, items=None, **kwargs):
    items = items or context.get('items')
    links = []
    for item in items:
        name = item.get('name')
        links.append({
            'text': item.get('name'),
            'url': '#{slug}'.format(slug=slugify(name)),
        })
    context = {
        'links': links,
    }
    context.update(kwargs)
    return render_to_string('styleguide/atoms/toc.html', context=context)


@register.simple_tag(takes_context=True)
def atom(context, atom=None, **kwargs):
    request = context.get('request')
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
    print(request)
    atom_output = render_to_string(template, context=atom_context, request=request)
    return atom_meta + atom_output
