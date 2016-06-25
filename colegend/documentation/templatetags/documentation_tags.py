from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag()
def documentation(documentation, classes=None):
    documentation_template = 'blog/widgets/documentation.html'
    documentation_context = {
        'title': documentation,
        'url': documentation.url,
        'classes': classes or '',
        'color': documentation.color or documentation.DARK,
    }
    return render_to_string(documentation_template, context=documentation_context)
