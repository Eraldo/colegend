from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def card(context, card=None, **kwargs):
    card = card or context.get('card')
    card_context = {
        'card': card
    }
    card_context.update(kwargs)
    card_template = 'molecules/card.html'
    return render_to_string(card_template, context=card_context)
