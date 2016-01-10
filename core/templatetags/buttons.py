from django import template
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def button(context, button=None):
    if not button:
        button = context.get('button')
    context = {
        'name': button.name,
        'url': button.url,
        'kind': button.kind,
        'locked': button.locked,
    }
    template = 'core/widgets/button.html'
    return render_to_string(template, context=context)
