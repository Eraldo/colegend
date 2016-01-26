from django import template
from django.template.loader import render_to_string

from colegend.core.utils.markdown import render

register = template.Library()


@register.simple_tag(takes_context=True)
def dayentry_link(context, dayentry=None, **kwargs):
    dayentry = dayentry or context.get('dayentry')
    context = {
        'name': dayentry,
        'url': dayentry.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'dayentries/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def dayentry_card(context, dayentry=None, **kwargs):
    dayentry = dayentry or context.get('dayentry')
    context = {
        'id': dayentry.id,
        'date': dayentry.date,
        'weekday': 'Monday',
        'locations': dayentry.locations,
        'content': render(dayentry.content),
        'detail_url': dayentry.detail_url,
        'update_url': dayentry.update_url,
        'delete_url': dayentry.delete_url,
        'tags': ['tag1', 'tag2'],
        'keywords': 'keyword1, keyword2, keyword3, keyword4',
    }
    context.update(kwargs)
    template = 'dayentries/widgets/card.html'
    return render_to_string(template, context=context)
