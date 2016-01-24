from django import template

from colegend.core.utils.markdown import render

register = template.Library()


@register.filter
def markdown(value):
    return render(value)
