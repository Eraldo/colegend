from django import template
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def menu(context, user=None):
    if not user:
        user = context.get('user')
    if user.is_authenticated():
        template = '_menu.html'
        context['journal'] = user.has_checkpoint('storytime')
        context['cloud_guide'] = user.has_checkpoint('cloud guide card')
        context['dream_team'] = False
        context['chat'] = user.has_checkpoint('chat card')
        context['virtual_room'] = user.has_checkpoint('virtual room')
        context['guidelines'] = user.has_checkpoint('guidelines card')
    else:
        template = '_menu_anonymous.html'
        context = {}
    return render_to_string(template, context=context)
