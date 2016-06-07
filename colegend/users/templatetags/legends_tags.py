from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from colegend.core.templatetags.core_tags import avatar, link

register = template.Library()


@register.simple_tag(takes_context=True)
def legend(context, legend=None, size=None, show_avatar=True, show_link=True, url=None):
    legend = legend or context.get('legend', context.get('user'))

    name = legend if legend.is_authenticated() else 'Anonymous'
    url = url or legend.get_absolute_url() if legend.is_authenticated() else reverse('join')

    legend_context = {
        'name': name,
        'url': url,
    }

    if show_avatar:
        if legend.is_authenticated() and legend.avatar:
            image = legend.get_avatar(size=size).url
        else:
            image = static('legends/images/anonymous.png')
        legend_context['avatar'] = avatar(image=image, name=name, url=url, classes=size)

    if show_link:
        legend_context['link'] = link(content=name, url=url)

    legend_template = 'legends/widgets/legend.html'
    return render_to_string(legend_template, context=legend_context)


@register.simple_tag()
def npc(name, size='large', show_avatar=True, show_link=True, url=None):
    npcs = {
        'coralina': {
            'name': 'Coralina',
            'file': 'Coralina.png',
        },
        'phoenix': {
            'name': 'Light Phoenix Oracle',
            'file': 'phoenix.png',
            'category': 7,
        },
        'eagle': {
            'name': 'Professor Eagle Scientist',
            'file': 'eagle.png',
            'category': 6,
        },
        'parrot': {
            'name': 'Moderating Parrot Poet',
            'file': 'parrot.png',
            'category': 5,
        },
        'monkey': {
            'file': 'monkey.png',
            'name': 'Caring Monkey Mother',
            'category': 4,
        },
        'tiger': {
            'name': 'Trillionaire Tiger Entrepreneur',
            'file': 'tiger.png',
            'category': 3,
        },
        'dolphin': {
            'name': 'Playful Dolphin Dancer',
            'file': 'dolphin.png',
            'category': 2,
        },
        'bear': {
            'name': 'Healthy Bear Athlete',
            'file': 'bear.png',
            'category': 1,
        },
    }
    name = name.lower()

    if name not in npcs:
        return ''

    npc = npcs.get(name)
    file = npc.get('file')
    image = static('legends/images/npc/{file}'.format(file=file))
    full_name = npc.get('name')
    category = npc.get('category')
    if category:
        classes = '{size} bg-category-{category}'.format(size=size, category=category)
    else:
        classes = '{size}'.format(size=size)

    npc_context = {
        'avatar': avatar(image=image, name=full_name, classes=classes),
        'link': link(content=full_name, url='#{}'.format(name)),
    }
    npc_template = 'legends/widgets/npc.html'
    return render_to_string(npc_template, npc_context)
