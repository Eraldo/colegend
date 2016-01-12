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
        context['cloud_guide'] = user.connected.guide_introduction or user.game.has_card('cloud guide')
        context['dream_team'] = False
        context['chat'] = user.connected.chat_introduction or user.game.has_card('chat')
        context['virtual_room'] = user.connected.virtual_room
        context['guidelines'] = user.connected.guidelines or user.game.has_card('guidelines')
    else:
        template = '_menu_anonymous.html'
        context = {}
    return render_to_string(template, context=context)
