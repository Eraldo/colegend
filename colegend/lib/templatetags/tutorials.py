from django import template
from django.template.loader import render_to_string
from tutorials.models import get_tutorial

register = template.Library()

__author__ = 'eraldo'


@register.simple_tag
def tutorial_link(tutorial_name):
    tutorial = get_tutorial(tutorial_name)
    if tutorial:
        link = render_to_string("tutorials/_tutorial_link.html", {'tutorial': tutorial})
        return link
    return ""
