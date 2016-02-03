from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def tag_link(context, tag=None, **kwargs):
    tag = tag or context.get('tag')
    context = {
        'name': tag,
        'url': tag.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'tags/widgets/link.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def tag(context, tag=None, **kwargs):
    tag = tag or context.get('tag')
    context = {
        'name': tag,
        'url': tag.get_absolute_url(),
    }
    context.update(kwargs)
    template = 'tags/widgets/tag.html'
    return render_to_string(template, context=context)
