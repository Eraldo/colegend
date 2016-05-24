from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def outcome_link(context, outcome=None, **kwargs):
    outcome = outcome or context.get('outcome')
    context = {
        'name': outcome,
        'url': outcome.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'outcomes/widgets/link.html'
    return render_to_string(template, context=context)
