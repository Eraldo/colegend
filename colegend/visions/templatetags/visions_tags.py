from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def vision_link(context, vision=None, **kwargs):
    vision = vision or context.get('vision')
    context = {
        'name': vision,
        'url': vision.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'visions/widgets/link.html'
    return render_to_string(template, context=context)
