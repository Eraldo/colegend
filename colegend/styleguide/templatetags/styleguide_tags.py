import pprint

from django import template
from django.template import Template, RequestContext
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


@register.simple_tag(takes_context=True)
def meta_widget(context, widget=None, **kwargs):
    request = context.get('request')
    widget = widget or context.get('widget')
    name = widget.get('name')
    tag = widget.get('tag')
    template = widget.get('template')
    widget_context = widget.get('context')
    context = {
        'name': name,
        'tag': tag,
        'context': pprint.pformat(widget_context),
    }
    context.update(kwargs)
    widget_meta = render_to_string('styleguide/widgets/meta.html', context=context)
    if template:
        widget_output = render_to_string(template, context=widget_context, request=request)
    else:
        template = Template('{{% load styleguide_widgets_tags %}}{{% {tag} {tag}={tag} %}}'.format(tag=tag))
        widget_context.update({'{}'.format(tag): widget_context})
        widget_output = template.render(context=RequestContext(request, widget_context))
    return widget_meta + widget_output
