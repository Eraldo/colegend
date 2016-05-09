from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def buttons(context, buttons=None, **kwargs):
    buttons = buttons or context.get('buttons')
    buttons_context = {
        'buttons': buttons
    }
    buttons_context.update(kwargs)
    buttons_template = 'molecules/buttons.html'
    return render_to_string(buttons_template, context=buttons_context)
