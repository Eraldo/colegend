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
                'name': 'conscious',
                'id': 'conscious',
                'icon': 'conscious',
                'items': [
                    {
                        'name': 'Dashboard',
                        'url': reverse('conscious:index'),
                    },
                    {
                        'name': 'divider',
                    },
                    {
                        'name': 'Journal',
                        'locked': not user.has_checkpoint('storytime'),
                        'url': reverse('journals:index'),
                    },
                    {
                        'name': 'Manager',
                        'locked': True,
                    },
                    {
                        'name': 'Habits',
                        'locked': True,
                    },
                    {
                        'name': 'divider',
                    },
                    {
                        'name': 'Tags',
                        'locked': not user.has_checkpoint('storytime'),
                        'url': reverse('tags:list'),
                    },
                ],
            },
            {
                'name': 'connected',
                'id': 'connected',
                'icon': 'connected',
                'items': [
                    {
                        'name': 'Dashboard',
                        'url': reverse('connected:index'),
                    },
                    {
                        'name': 'divider',
                    },
                    {
                        'name': 'Legend',
                        'url': reverse('legends:detail', args=[user.username]),
                    },
                    {
                        'name': 'Cloud Guide',
                        'locked': not user.has_checkpoint('cloud guide card'),
                        'url': reverse('guides:guide'),
                    },
                    {
                        'name': 'Dream Team',
                        'locked': True,
                    },
                    {
                        'name': 'Tribe',
                        'locked': True,
                    },
                    {
                        'name': 'Circle',
                        'locked': True,
                    },
                    {
                        'name': 'divider',
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
                        'external': True,
                    },
                ],
            },
            {
                'name': 'continuous',
                'id': 'continuous',
                'icon': 'continuous',
                'items': [
                    {
                        'name': 'Dashboard',
                        'url': reverse('continuous:index'),
                    },
                    {
                        'name': 'divider',
                    },
                    {
                        'name': 'Game',
                        'url': reverse('games:index'),
                    },
                    {
                        'name': 'Story',
                        'url': reverse('story:index'),
                    },
                    {
                        'name': 'Personal Story',
                        'locked': True,
                    },
                    {
                        'name': 'Tribe Story',
                        'locked': True,
                    },
                    {
                        'name': 'coLegend Story',
                        'locked': True,
                    },
                ],
            },
        ]
        context['dropdowns'] = dropdowns
        account_items = [
            {
                'name': 'Legend',
                'url': reverse('legends:detail', args=[user.username]),
                'icon': 'legend',
            },
            {
                'name': 'Support',
                'url': reverse('support:index'),
                'icon': 'support',
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
