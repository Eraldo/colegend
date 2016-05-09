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
def meta_element(context, element=None, **kwargs):
    request = context.get('request')
    element = element or context.get('element')
    name = element.get('name')
    template = element.get('template')
    element_context = element.get('context')
    context = {
        'name': name,
        'template': template,
        'context': pprint.pformat(element_context),
    }
    context.update(kwargs)
    element_meta = render_to_string('styleguide/atoms/meta.html', context=context)
    element_output = render_to_string(template, context=element_context, request=request)
    return element_meta + element_output
