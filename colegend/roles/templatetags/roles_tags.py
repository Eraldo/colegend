from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def role_link(context, role=None, **kwargs):
    role = role or context.get('role')
    context = {
        'name': role,
        'url': role.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'roles/widgets/link.html'
    return render_to_string(template, context=context)
