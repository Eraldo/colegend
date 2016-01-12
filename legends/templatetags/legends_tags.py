from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag(takes_context=True)
def legend(context, legend=None, size=None):
    if not legend:
        legend = context.get('legend')

    context = {
        'name': legend.owner,
        'url': legend.get_absolute_url(),
    }

    template = 'legends/widgets/link.html'

    if size:
        context['size'] = size
        if legend.avatar:
            context['source'] = legend.get_avatar(size=size).url
        template = 'legends/widgets/legend.html'
    return render_to_string(template, context=context)


@register.simple_tag()
def npc(name):
    template = 'legends/widgets/legend.html'
    context = {
        'name': name,
        'source': static('legends/images/npc/{name}.png'.format(name=name)),
    }
    return render_to_string(template, context)
