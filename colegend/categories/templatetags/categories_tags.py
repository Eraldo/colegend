from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def category_link(context, category=None, **kwargs):
    category = category or context.get('category')
    context = {
        'name': category,
        'url': category.detail_url,
    }
    context.update(kwargs)
    template = 'categories/widgets/link.html'
    return render_to_string(template, context=context)
