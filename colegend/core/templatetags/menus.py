from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

register = template.Library()

__author__ = 'Eraldo Energy'


@register.simple_tag(takes_context=True)
def menu(context, user=None, name='main'):
    user = user or context.get('user')
    if name == 'main':
        template = 'widgets/menu.html'
    elif name == 'account':
        template = 'widgets/submenu.html'
    menu_context = {}
    if user.is_authenticated():
        if name == 'main':
            menu_context['nodes'] = [
                {
                    'name': 'Apps',
                    'nodes': [
                        {
                            'name': 'Manager',
                            'url': reverse('manager:index'),
                        },
                        {
                            'name': 'Journal',
                            'locked': not user.has_checkpoint('storytime'),
                            'url': reverse('journals:index'),
                        },
                        {
                            'name': 'Story',
                            'url': reverse('story:index'),
                        },
                        {
                            'name': 'Vision',
                            'url': reverse('visions:index'),
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
                            'name': 'Habits',
                            'locked': True,
                        },
                    ],
                },
                {
                    'name': 'Community',
                    'nodes': [
                        {
                            'name': 'Legend',
                            'url': reverse('legends:detail', args=[user.username]),
                        },
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
                            'url': reverse('chat:index'),
                            'external': user.has_checkpoint('chat'),
                        },
                        {
                            'name': 'Virtual Room',
                            'locked': not user.has_checkpoint('virtual room'),
                            'url': reverse('chat:room'),
                            'external': True,
                        },
                        {
                            'name': 'Guidelines',
                            'locked': not user.has_checkpoint('guidelines card'),
                            'url': reverse('guidelines:index'),
                        },
                    ],
                },
                {
                    'name': 'Project',
                    'nodes': [
                        {
                            'name': 'About',
                            'url': reverse('about'),
                        },
                        {
                            'name': 'Events',
                            'url': reverse('events:index'),
                        },
                        {
                            'name': 'Support',
                            'url': reverse('support:index'),
                        },
                        {
                            'name': 'News',
                            'locked': True,
                        },
                        {
                            'name': 'Roles',
                            'url': reverse('roles:index'),
                        },
                        {
                            'name': 'Styleguide',
                            'locked': not user.is_staff,
                            'url': reverse('styleguide:index'),
                        },
                    ],
                },
            ]
        elif name == 'account':
            menu_context['nodes'] = [
                {
                    'name': 'Profile',
                    'url': reverse('legends:detail', args=[user.username]),
                },
                {
                    'name': 'Settings',
                    'url': reverse('legends:settings'),
                },
                {
                    'name': 'Logout',
                    'url': reverse('account_logout'),
                },
            ]
    else:
        if name == 'main':
            menu_context['nodes'] = [
                {
                    'name': 'Join',
                    'url': reverse('join'),
                },
                {
                    'name': 'Log in',
                    'url': reverse('account_login'),
                },
            ]
        elif name == 'account':
            menu_context['nodes'] = [
                {
                    'name': 'Join',
                    'url': reverse('join'),
                },
                {
                    'name': 'Log in',
                    'url': reverse('account_login'),
                },
            ]
    return render_to_string(template, context=menu_context)


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
