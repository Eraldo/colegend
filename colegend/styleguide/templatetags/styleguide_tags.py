import pprint

from django import template
from django.template import Template, RequestContext
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def toc(context, elements=None, **kwargs):
    elements = elements or context.get('elements', {})
    links = []
    for element in elements:
        name = element.name
        links.append({
            'text': name,
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
    tag = element.get('tag')
    template = element.get('template')
    element_context = element.get('context')
    context = {
        'name': name,
        'tag': tag,
        'context': pprint.pformat(element_context),
    }
    context.update(kwargs)
    element_meta = render_to_string('styleguide/atoms/meta.html', context=context)
    if template:
        element_output = render_to_string(template, context=element_context, request=request)
    else:
        template = Template('{{% load atoms_tags %}}{{% {tag} {tag}={tag} %}}'.format(tag=tag))
        element_context.update({'{}'.format(tag): element_context})
        element_output = template.render(context=RequestContext(request, element_context))
    return element_meta + element_output
