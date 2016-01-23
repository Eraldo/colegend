from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def button(context, button=None):
    if not button:
        button = context.get('button')
    context = {
        'name': button.name,
        'url': button.url,
        'kind': button.kind,
        'locked': button.locked,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def create_button(context, name='create', pattern=None, url=None, kind='secondary btn-sm', locked=False):
    if not url and pattern:
        url = reverse(pattern)
    context = {
        'id': name,
        'url': url,
        'kind': kind,
        'icon': name,
        'locked': locked,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def detail_button(context, name='detail', pattern=None, url=None, kind='secondary btn-sm', locked=False):
    if not url and pattern:
        url = reverse(pattern)
    context = {
        'id': name,
        'url': url,
        'kind': kind,
        'icon': name,
        'locked': locked,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def update_button(context, name='update', pattern=None, url=None, kind='primary btn-sm', locked=False):
    if not url and pattern:
        url = reverse(pattern)
    context = {
        'id': name,
        'url': url,
        'kind': kind,
        'icon': name,
        'locked': locked,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def delete_button(context, name='delete', pattern=None, url=None, kind='danger btn-sm', locked=False):
    if not url and pattern:
        url = reverse(pattern)
    context = {
        'id': name,
        'url': url,
        'kind': kind,
        'icon': name,
        'locked': locked,
    }
    template = 'widgets/button.html'
    return render_to_string(template, context=context)
