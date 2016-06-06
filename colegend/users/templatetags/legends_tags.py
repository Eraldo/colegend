from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

register = template.Library()


# Future: Refactor this tag to a shortcut reusing the other tags.
@register.simple_tag(takes_context=True)
def legend(context, legend=None, size=None, **kwargs):
    # if no legend is given take the legend from the context or else the user
    legend = legend or context.get('legend', context.get('user'))
    if not legend.is_authenticated():
        # TODO: return anonymous / context avatar
        return ''

    url = kwargs.get('url', legend.get_absolute_url())

    context = {
        'name': legend,
        'url': url,
        'id': slugify(legend.username),
    }
    context.update(kwargs)
    template = 'legends/widgets/link.html'
    if size:
        context['size'] = size
        if legend.avatar:
            context['source'] = legend.get_avatar(size=size).url
        template = 'legends/widgets/legend.html'
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def legend_avatar(context, legend=None, size=None, **kwargs):
    # if no legend is given take the legend from the context or else the user
    legend = legend or context.get('legend', context.get('user'))
    size = size or context.get('size', 'medium')
    legend_context = {
        'label': {
            'class': 'label-pill bg-accent',
        },
        'size': size,
    }
    if legend and legend.is_authenticated():
        legend_context.update({
            'name': legend,
            'image': legend.get_avatar(size=size).url if legend.avatar else static('legends/images/anonymous.png'),
            'url': legend.get_absolute_url(),
        })
    else:
        legend_context.update({
            'name': 'Anonymous',
            'image': static('legends/images/anonymous.png'),
        })
    legend_context.update(kwargs)
    template = 'legends/widgets/avatar.html'
    return render_to_string(template, context=legend_context)


@register.simple_tag(takes_context=True)
def legend_link(context, legend=None, size=None, **kwargs):
    # if no legend is given take the legend from the context or else the user
    legend = legend or context.get('legend', context.get('user'))
    legend_context = {}
    if legend and legend.is_authenticated():
        legend_context.update({
            'content': legend,
            'url': legend.get_absolute_url(),
        })
    else:
        legend_context.update({
            'content': 'Anonymous',
            'url': reverse('join'),
        })
    legend_context.update(kwargs)
    template = 'widgets/link.html'
    return render_to_string(template, context=legend_context)


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
        'dolphin': 'dolphin.png',
        'bear': 'bear.png',
    }
    names = {
        'coralina': 'Coralina',
        'phoenix': 'Light Phoenix Oracle',
        'eagle': 'Professor Eagle Scientist',
        'parrot': 'Moderating Parrot Poet',
        'monkey': 'Caring Monkey Mother',
        'tiger': 'Trillionaire Tiger Entrepreneur',
        'dolphin': 'Playful Dolphin Dancer',
        'bear': 'Healthy Bear Athlete',
    }
    image_name = images.get(name) or images.get(name.lower())
    full_name = names.get(name, name)
    context = {
        'name': full_name,
        'source': static('legends/images/npc/{image_name}'.format(image_name=image_name)),
        'classname': name,
    }
    return render_to_string(template, context)
