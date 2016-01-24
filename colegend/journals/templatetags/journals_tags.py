from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def journal_link(context, journal=None):
    if not journal:
        journal = context.get('journal')
    context = {
        'name': journal,
        'url': journal.get_absolute_url(),
    }
    template = 'journals/widgets/link.html'
    return render_to_string(template, context=context)
