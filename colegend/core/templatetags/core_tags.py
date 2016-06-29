from django import template
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.html import format_html

from colegend.core.intuitive_duration.utils import intuitive_duration_string
from colegend.core.utils.icons import get_icon_class

register = template.Library()


@register.filter
def intuitive_duration(value):
    try:
        return intuitive_duration_string(value)
    except ValidationError:
        return ''


@register.simple_tag()
def label(content, classes='label-default'):
    label_template = 'widgets/label.html'
    label_context = {
        'content': content,
        'classes': classes,
    }
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
def image(url, name=None, classes='', responsive=True):
    image_template = 'widgets/image.html'
    if responsive:
        classes += ' img-responsive'
    image_context = {
        'url': url,
        'name': name,
        'classes': classes,
    }
    return render_to_string(image_template, context=image_context)


@register.simple_tag()
def heading(content, level=1, classes=None):
    heading_template = 'widgets/heading.html'
    heading_context = {
        'level': level,
        'content': content,
        'classes': classes or '',
    }
    return render_to_string(heading_template, context=heading_context)


@register.simple_tag
def icon(name, prefix='fa', large=False, fixed=False, spin=False, pulse=False, list=False,
         rotate=0, border=False, color=None, classes=None, raw=False):
    icon = get_icon_class(name)
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
        icon += ' {}'.format(classes)
    if raw:
        return icon
    context = {
        'classes': icon,
        'color': color,
    }
    return render_to_string('widgets/icon.html', context=context)


render_icon = icon


@register.simple_tag()
def button(name, url=None, pattern=None, prefix='btn', content=None, classes='btn-primary', icon=None, size=None, locked=False, external=False, attributes=None):
    classes_dict = {
        'list': 'btn-secondary btn-sm',
        'create': 'btn-secondary btn-sm',
        'detail': 'btn-secondary btn-sm',
        'update': 'btn-secondary btn-sm',
        'delete': 'btn-danger btn-sm',
    }
    if prefix:
        classes = '{} {}'.format(prefix, classes)
    if name in classes_dict:
        # TODO: refactor to overwrite classes and the size variable
        classes += ' {}'.format(classes_dict.get('name'))
        if not icon:
            icon = name

    if size:
        sizes = {
            'small': 'btn-sm',
            'large': 'btn-lg',
        }
        size_class = sizes.get(size, '')
        if size_class:
            classes += ' {}'.format(size_class)
    if pattern and not url:
        url = reverse(pattern)
    if locked:
        icon = 'locked'
        url = None
        classes += ' disabled'

    if not content:
        content = name
    if icon:
        content = format_html(
            '{icon} {content}', icon=render_icon(icon, fixed=True), content=content)

    context = {
        'url': url,
        'classes': classes,
        'content': content,
        'external': external,
        'attributes': attributes,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag()
def speech_bubble(content, direction='left', arrow_classes=None, responsive=False):
    speech_bubble_template = 'widgets/speech-bubble.html'
    speech_bubble_context = {
        'arrow': '{direction}{classes}'.format(direction=direction,
                                               classes=' {}'.format(arrow_classes) if arrow_classes else ''),
        'responsive_arrow': 'up' if responsive else '',
        'content': content,
    }
    return render_to_string(speech_bubble_template, context=speech_bubble_context)


@register.simple_tag()
def buttons(buttons, classes=None):
    buttons_template = 'widgets/buttons.html'
    buttons_context = {
        'buttons': buttons,
        'classes': classes or '',
    }
    return render_to_string(buttons_template, context=buttons_context)


@register.simple_tag()
def card(content, header=None, title=None, footer=None, url=None, classes=None):
    card_template = 'widgets/card.html'
    card_context = {
        'header': header,
        'content': content,
        'footer': footer,
        'classes': classes or '',
    }
    return render_to_string(card_template, context=card_context)
