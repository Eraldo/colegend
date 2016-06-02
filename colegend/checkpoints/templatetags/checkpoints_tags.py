from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def has_checkpoints(context, user=None, *args, **kwargs):
    user = user or context.get('request').user
    checkpoints = args
    if isinstance(checkpoints, str):
        checkpoints = [checkpoints]
    for checkpoint in checkpoints:
        if not user.has_checkpoint(checkpoint):
            return False
    return True
