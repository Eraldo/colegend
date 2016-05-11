from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def button(context, button=None, **kwargs):
    button = button or context.get('button')
    button_context = {
        'url': button.get('url'),
        'class': button.get('class'),
        'icon': button.get('icon'),
        'text': button.get('text'),
    }
    button_context.update(kwargs)
    button_template = 'atoms/button.html'
    return render_to_string(button_template, context=button_context)


@register.simple_tag(takes_context=True)
def label(context, label=None, **kwargs):
    label = label or context.get('label', {})
    label_context = {
        'class': label.get('class'),
        'text': label.get('text'),
    }
    label_context.update(kwargs)
    label_template = 'atoms/label.html'
    return render_to_string(label_template, context=label_context)


@register.simple_tag(takes_context=True)
def breadcrumb(context, breadcrumb=None, **kwargs):
    breadcrumb = breadcrumb or context.get('breadcrumb')
    breadcrumb_context = {
        'name': breadcrumb.get('name'),
        'url': breadcrumb.get('url'),
    }
    breadcrumb_context.update(kwargs)
    breadcrumb_template = 'atoms/breadcrumb.html'
    return render_to_string(breadcrumb_template, context=breadcrumb_context)
