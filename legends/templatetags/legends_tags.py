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
    images = {
        'coralina': 'Coralina.png',
        'phoenix': 'phoenix.png',
        'eagle': 'eagle.png',
        'parrot': 'parrot.png',
        'monkey': 'monkey.png',
        'tiger': 'tiger.png',
        'dolphin': 'cangaroo.png',
        'bear': 'bear.png',
    }
    names = {
        'coralina': 'Coralina',
        'phoenix': 'phoenix.png',
        'eagle': 'eagle.png',
        'parrot': 'parrot.png',
        'monkey': 'monkey.png',
        'tiger': 'tiger.png',
        'dolphin': 'cangaroo.png',
        'bear': 'bear.png',
    }
    image_name = images.get(name) or images.get(name.lower())
    context = {
        'name': name,
        'source': static('legends/images/npc/{image_name}'.format(image_name=image_name)),
    }
    return render_to_string(template, context)
