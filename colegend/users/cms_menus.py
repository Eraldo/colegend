from django.core.urlresolvers import reverse
from menus.base import NavigationNode, Menu
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _


class UserMenu(Menu):
    name = _('User menu')

    def get_nodes(self, request):
        user = request.user
        nodes = []
        if user.is_authenticated():
            nodes = [
                NavigationNode(
                    title=_('Profile'),
                    url=reverse('legends:detail', args=[user.username]),
                    id='profile',
                ),
                NavigationNode(
                    title=_('Settings'),
                    url=reverse('legends:settings'),
                    id='settings',
                ),
                NavigationNode(
                    title=_('Logout'),
                    url=reverse('account_logout'),
                    id='logout',
                ),
            ]
        else:
            nodes = [
                NavigationNode(
                    title=_('Join'),
                    url=reverse('join'),
                    id='join',
                ),
                NavigationNode(
                    title=_('Login'),
                    url=reverse('account_login'),
                    id='login',
                ),
            ]
        return nodes


menu_pool.register_menu(UserMenu)
