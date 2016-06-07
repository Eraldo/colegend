from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import render_to_string

from colegend.core.templatetags.core_tags import avatar, link

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


@register.simple_tag(takes_context=True)
def role(context, role=None, size=None, show_avatar=True, show_link=True, url=None):
    role = role or context.get('role')

    if not role: return ''

    name = role
    url = url or role.get_absolute_url()
    classes = 'bg-main-light {size}'.format(size=size)

    role_context = {
        'name': name,
        'url': url,
    }

    if show_avatar:
        if role.icon:
            image = role.icon.url
        else:
            image = static('roles/images/icon_object_f.png')
        role_context['avatar'] = avatar(image=image, name=name, url=url, classes=classes)

    if show_link:
        role_context['link'] = link(content=name, url=url)

    role_template = 'roles/widgets/role.html'
    return render_to_string(role_template, context=role_context)
