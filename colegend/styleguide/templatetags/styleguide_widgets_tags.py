from django import template
from django.template.loader import render_to_string

from colegend.core.templatetags.core_tags import icon

register = template.Library()


@register.simple_tag(takes_context=True)
def button(context, button=None, **kwargs):
    button = button or context.get('button', {})
    content = button.get('content')
    icon_name = button.get('icon')
    if icon_name:
        content = '{icon} {content}'.format(
            icon=icon(context, icon_name),
            content=content
        )
    button_context = {
        'url': button.get('url'),
        'classes': button.get('classes'),
        'content': content,
    }
    button_context.update(kwargs)
    button_template = 'widgets/button.html'
    return render_to_string(button_template, context=button_context)


@register.simple_tag(takes_context=True)
def label(context, label=None, **kwargs):
    label = label or context.get('label', {})
    label_context = label
    label_context.update(kwargs)
    label_template = 'widgets/label.html'
    return render_to_string(label_template, context=label_context)


@register.simple_tag(takes_context=True)
def breadcrumb(context, breadcrumb=None, **kwargs):
    breadcrumb = breadcrumb or context.get('breadcrumb')
    breadcrumb_context = {
        'name': breadcrumb.get('name'),
        'url': breadcrumb.get('url'),
    }
    breadcrumb_context.update(kwargs)
    breadcrumb_template = 'widgets/breadcrumb.html'
    return render_to_string(breadcrumb_template, context=breadcrumb_context)


@register.simple_tag(takes_context=True)
def buttons(context, buttons=None, **kwargs):
    buttons = buttons or context.get('buttons')
    buttons_context = {
        'buttons': buttons
    }
    buttons_context.update(kwargs)
    buttons_template = 'widgets/buttons.html'
    return render_to_string(buttons_template, context=buttons_context)


@register.simple_tag(takes_context=True)
def card(context, card=None, **kwargs):
    card = card or context.get('card')
    card_context = {
        'card': card
    }
    card_context.update(kwargs)
    card_template = 'widgets/card.html'
    return render_to_string(card_template, context=card_context)
