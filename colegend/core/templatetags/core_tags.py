from django import template
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string

from colegend.core.intuitive_duration.utils import intuitive_duration_string

register = template.Library()


@register.filter
def intuitive_duration(value):
    try:
        return intuitive_duration_string(value)
    except ValidationError:
        return ''


@register.simple_tag(takes_context=True)
def label(context, label=None, **kwargs):
    label = label or context.get('label', {})
    label_context = label
    label_context.update(kwargs)
    label_template = 'widgets/label.html'
    return render_to_string(label_template, context=label_context)


@register.simple_tag()
def avatar(image, name=None, url=None, classes=None):
    avatar_template = 'widgets/avatar.html'
    avatar_context = {
        'image': image,
        'name': name,
        'classes': classes,
        'url': url,
    }
    return render_to_string(avatar_template, context=avatar_context)


@register.simple_tag()
def link(content, url, external=False):
    link_context = {
        'content': content,
        'url': url,
        'external': external,
    }
    link_template = 'widgets/link.html'
    return render_to_string(link_template, context=link_context)
