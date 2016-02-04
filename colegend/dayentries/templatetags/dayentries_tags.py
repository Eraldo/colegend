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
    if dayentry:
        context = {
            'id': dayentry.id,
            'date': dayentry.date,
            'weekday': dayentry.date.strftime('%a'),
            'weekday_number': dayentry.date.isoweekday(),
            'locations': dayentry.locations,
            'content': render(dayentry.content),
            'actions': True,
            'detail_url': dayentry.detail_url,
            'update_url': dayentry.update_url,
            'delete_url': dayentry.delete_url,
            'keywords': dayentry.keywords,
            'tags': dayentry.tags.all(),
        }
    context.update(kwargs)
    template = 'dayentries/widgets/card.html'
    return render_to_string(template, context=context)
