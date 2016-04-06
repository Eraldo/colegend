from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def donation_link(context, donation=None, **kwargs):
    donation = donation or context.get('donation')
    context = {
        'name': donation,
        'url': donation.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'donations/widgets/link.html'
    return render_to_string(template, context=context)
