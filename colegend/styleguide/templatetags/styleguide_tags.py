import pprint

from django import template
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def toc(context, widgets=None, **kwargs):
    widgets = widgets or context.get('widgets', {})
    links = []
    for widget in widgets:
        name = widget.name
        links.append({
            'text': name,
            'url': '#{slug}'.format(slug=slugify(name)),
        })
    context = {
        'links': links,
    }
    context.update(kwargs)
    return render_to_string('styleguide/widgets/toc.html', context=context)
