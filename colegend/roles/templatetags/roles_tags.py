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


@register.simple_tag(takes_context=True)
def has_roles(context, user=None, *args, **kwargs):
    user = user or context.get('request').user
    roles = args
    if isinstance(roles, str):
        roles = [roles]
    for role in roles:
        if not user.has_role(role):
            return False
    return True
