from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def menu(context, user=None):
    if not user:
        user = context.get('user')
    if user and user.is_authenticated():
        template = 'widgets/menu/authenticated.html'
        dropdowns = [
            {
                'name': 'Apps',
                'id': 'conscious',
                'icon': 'cubes',
                'class': 'text-conscious',
                'items': [
                    {
                        'name': 'Manager',
                        'locked': True,
                    },
                    {
                        'name': 'Journal',
                        'locked': not user.has_checkpoint('storytime'),
                        'url': reverse('journals:index'),
                    },
                    {
                        'name': 'Vision',
                        'locked': True,
                    },
                    {
                        'name': 'Academy',
                        'locked': True,
                    },
                    {
                        'name': 'Game',
                        'url': reverse('games:index'),
                    },
                    {
                        'name': 'Story',
                        'url': reverse('story:index'),
                    },
                ],
            },
            {
                'name': 'Community',
                'id': 'community',
                'icon': 'group',
                'class': 'text-connected',
                'items': [
                    {
                        'name': 'Duo',
                        'locked': True,
                    },
                    {
                        'name': 'Tribe',
                        'locked': True,
                    },
                    {
                        'name': 'Clan',
                        'locked': True,
                    },
                    {
                        'name': 'Guide',
                        'locked': not user.has_checkpoint('cloud guide card'),
                        'url': reverse('guides:guide'),
                    },
                    {
                        'name': 'Chat',
                        'locked': not user.has_checkpoint('chat card'),
                        'url': reverse('connected:chat'),
                        'external': user.has_checkpoint('chat'),
                    },
                    {
                        'name': 'Virtual Room',
                        'locked': not user.has_checkpoint('virtual room'),
                        'url': reverse('connected:virtual-room'),
                        'external': True,
                    },
                    {
                        'name': 'Guidelines',
                        'locked': not user.has_checkpoint('guidelines card'),
                        'url': reverse('connected:guidelines'),
                    },
                ],
            },
            {
                'name': 'Project',
                'id': 'project',
                'icon': 'info-circle',
                'class': 'text-continuous',
                'items': [
                    {
                        'name': 'About',
                        'url': reverse('about'),
                    },
                    # {
                    #     'name': 'Roles',
                    #     'url': reverse('roles:index'),
                    # },
                    # {
                    #     'name': 'Top Supporters',
                    #     'url': reverse('donations:top-supporters'),
                    # },
                    {
                        'name': 'Events',
                        'url': reverse('events:index'),
                    },
                    {
                        'name': 'Support',
                        'url': reverse('support:index'),
                    },
                    # {
                    #     'name': 'Framework',
                    #     'url': reverse('categories:index'),
                    # },
                    {
                        'name': 'News',
                        'locked': True,
                    },
                ],
            },
        ]
        context['dropdowns'] = dropdowns
        account_items = [
            {
                'name': 'Profile',
                'url': reverse('legends:detail', args=[user.username]),
                'icon': 'legend',
            },
            {
                'name': 'Settings',
                'url': reverse('legends:settings'),
                'icon': 'settings',
            },
            {
                'name': 'Logout',
                'url': reverse('account_logout'),
                'icon': 'sign-out',
            },
        ]
        context['account_items'] = account_items
        context['journal'] = user.has_checkpoint('storytime')
        context['cloud_guide'] = user.has_checkpoint('cloud guide card')
        context['dream_team'] = False
        context['chat'] = user.has_checkpoint('chat card')
        context['virtual_room'] = user.has_checkpoint('virtual room')
        context['guidelines'] = user.has_checkpoint('guidelines card')
    else:
        template = 'widgets/menu/anonymous.html'
        context = {}
    return render_to_string(template, context=context)


@register.simple_tag(takes_context=True)
def menu_item(context, item=None, **kwargs):
    item = item or context.get('item')
    if item:
        context = {
            'name': item.get('name'),
            'locked': item.get('locked'),
            'url': item.get('url'),
            'external': item.get('external'),
            'icon': item.get('icon'),
        }
    context.update(kwargs)
    template = 'widgets/menu/item.html'
    return render_to_string(template, context=context)
