from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _


class TestMenu(Menu):
    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('Page 1'), "#page1", 1)
        n2 = NavigationNode(_('Page 2'), "#page2", 2)
        n3 = NavigationNode(_('Page 3'), "#page3", 3)
        n4 = NavigationNode(_('Page 3.1'), "#page31", 4, 3)
        n5 = NavigationNode(_('Page 3.2'), "#page32", 5, 3)
        n6 = NavigationNode(_('Page 3.3'), "#page33", 6, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        nodes.append(n5)
        nodes.append(n6)
        return nodes


menu_pool.register_menu(TestMenu)
