from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def card(context, card=None, url=None):
    if not card:
        card = context.get('card')
    context = {
        'title': card.name,
        'content': card.content,
        'source': card.image.url if card.image else '',
        'id': card.id,
        'details': card.details,
        'url': url,
    }
    template = 'cards/widgets/card.html'
    return render_to_string(template, context=context)
