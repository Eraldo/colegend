from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def dayentry_link(context, dayentry=None):
    if not dayentry:
        dayentry = context.get('dayentry')
    context = {
        'name': dayentry,
        'url': dayentry.get_absolute_url(),
    }
    template = 'dayentries/widgets/link.html'
    return render_to_string(template, context=context)
