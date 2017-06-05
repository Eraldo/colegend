from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from wagtail.wagtailcore.templatetags.wagtailcore_tags import slugurl

from colegend.community.models import CommunityPage

register = template.Library()

__author__ = 'Eraldo Energy'


def get_community_url(group='duo'):
    community_page = CommunityPage.objects.first()
    if community_page:
        url = community_page.url
        if group != 'community':
            url += community_page.reverse_subpage(group)
    else:
        url = '#{0}'.format(group)
    return url


@register.simple_tag(takes_context=True)
def menu(context, user=None, name='main'):
    user = user or context.get('user')
    if name == 'main':
        template = 'widgets/menu.html'
    elif name == 'account':
        template = 'widgets/submenu.html'
    menu_context = {}
    menu_context['nodes'] = [
        {
            'name': 'Apps',
            'nodes': [
                {
                    'name': 'Home',
                    # 'locked': True,
                    'url': slugurl(context, slug='home'),
                },
                {
                    'name': 'Arcade',
                    # 'locked': True,
                    'url': slugurl(context, slug='arcade'),
                },
                {
                    'name': 'Office',
                    # 'url': reverse('office'),
                },
                {
                    'name': 'Community',
                    # 'url': reverse('community'),
                },
                {
                    'name': 'Studio',
                    # 'url': reverse('studio'),
                },
                {
                    'name': 'Academy',
                    # 'url': reverse('academy'),
                },
                {
                    'name': 'Journey',
                    # 'url': reverse('journey'),
                },
                {
                    'name': 'Manager',
                    'locked': not user.has_checkpoint('manager') if user.is_authenticated() else True,
                    'url': reverse('manager:index'),
                },
                {
                    'name': 'Journal',
                    'locked': not user.has_checkpoint('storytime') if user.is_authenticated() else True,
                    'url': slugurl(context, slug='journal'),
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
                    'name': 'Tutorial',
                    'url': reverse('games:index'),
                },
                {
                    'name': 'Habits',
                    'locked': True,
                },
                {
                    'name': 'Resources',
                    'url': slugurl(context, slug='personal-development-resources'),
                },
            ],
        },
        {
            'name': 'Community',
            'nodes': [
                {
                    'name': 'Legend',
                    'url': reverse('legends:detail', args=[user.username]) if user.is_authenticated() else '#profile',
                },
                {
                    'name': 'Duo',
                    # 'locked': not user.has_checkpoint('community'),
                    'url': get_community_url(group='duo'),
                },
                {
                    'name': 'Clan',
                    # 'locked': True,
                    'url': get_community_url(group='clan'),
                },
                {
                    'name': 'Tribe',
                    # 'locked': True,
                    'url': get_community_url(group='tribe'),
                },
                {
                    'name': 'Legends',
                    # 'locked': True,
                    'url': get_community_url(group='community'),
                },
                {
                    'name': 'Guide',
                    'locked': not user.has_checkpoint('cloud guide card') if user.is_authenticated() else True,
                    'url': reverse('guides:index'),
                },
                {
                    'name': 'Chat',
                    'locked': not user.has_checkpoint('chat card') if user.is_authenticated() else True,
                    'url': reverse('chat:index'),
                    'external': user.has_checkpoint('chat') if user.is_authenticated() else True,
                },
                {
                    'name': 'Virtual Room',
                    'locked': not user.has_checkpoint('virtual room') if user.is_authenticated() else True,
                    'url': reverse('chat:room'),
                    'external': True,
                },
                {
                    'name': 'Guidelines',
                    'locked': not user.has_checkpoint('guidelines card') if user.is_authenticated() else True,
                    'url': reverse('guidelines:index'),
                },
            ],
        },
        {
            'name': 'Project',
            'nodes': [
                {
                    'name': 'About',
                    'url': slugurl(context, 'about'),
                },
                {
                    'name': 'Events',
                    'url': slugurl(context, slug='events'),
                },
                {
                    'name': 'Support',
                    'url': slugurl(context, slug='support'),
                },
                {
                    'name': 'Blog',
                    'url': slugurl(context, slug='blog'),
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
    if user.is_authenticated():
        if name == 'main':
            pass
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
                    'url': slugurl(context, 'join'),
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
                    'url': slugurl(context, 'join'),
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
