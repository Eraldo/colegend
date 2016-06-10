from django import template
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string

from colegend.core.intuitive_duration.utils import intuitive_duration_string
from colegend.core.utils.icons import get_icon_class

register = template.Library()


@register.filter
def intuitive_duration(value):
    try:
        return intuitive_duration_string(value)
    except ValidationError:
        return ''


@register.simple_tag(takes_context=True)
def label(context, label=None, **kwargs):
    label_template = 'widgets/label.html'
    label = label or context.get('label', {})
    label_context = label
    label_context.update(kwargs)
    return render_to_string(label_template, context=label_context)


@register.simple_tag()
def link(content, url, external=False):
    link_template = 'widgets/link.html'
    link_context = {
        'content': content,
        'url': url,
        'external': external,
    }
    return render_to_string(link_template, context=link_context)


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
def image(url, name=None, classes=None):
    image_template = 'widgets/image.html'
    image_context = {
        'url': url,
        'name': name,
        'classes': classes,
    }
    return render_to_string(image_template, context=image_context)


@register.simple_tag()
def headline(content, level=1, classes=None):
    headline_template = 'widgets/headline.html'
    headline_context = {
        'level': level,
        'content': content,
        'classes': classes or '',
    }
    return render_to_string(headline_template, context=headline_context)


@register.simple_tag
def icon(name, prefix='fa', large=False, fixed=False, spin=False, pulse=False, list=False,
         rotate=0, border=False, color=None, classes=None, raw=False):
    name = get_icon_class(name)
    icon = '{prefix} {name}'.format(
        prefix=prefix,
        name=name,
    )
    if large:
        icon += ' {}-lg'.format(prefix)
    if fixed:
        icon += ' {}-fw'.format(prefix)
    if spin:
        icon += ' {}-spin'.format(prefix)
    if pulse:
        icon += ' {}-pulse'.format(prefix)
    if list:
        icon += ' {}-li'.format(prefix)
    if rotate:
        icon += ' {}-rotate-{}'.format(prefix, rotate)
    if border:
        icon += ' {}-border'.format(prefix)
    if classes:
        icon += ' {}-classes'.format(prefix)
    if raw:
        return icon
    context = {
        'classes': icon,
        'color': color,
    }
    return render_to_string('widgets/icon.html', context=context)


@register.simple_tag()
def speech_bubble(content, direction='left', arrow_classes=None, responsive=False):
    speech_bubble_template = 'widgets/speech-bubble.html'
    speech_bubble_context = {
        'arrow': '{direction}{classes}'.format(direction=direction, classes=' {}'.format(arrow_classes) if arrow_classes else ''),
        'responsive_arrow': 'up' if responsive else '',
        'content': content,
    }
    return render_to_string(speech_bubble_template, context=speech_bubble_context)
