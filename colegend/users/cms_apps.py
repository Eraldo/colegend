from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_menus import UserMenu


class LegendsApphook(CMSApp):
    name = _('Legends')
    urls = ['colegend.users.urls']
    menus = [UserMenu]


apphook_pool.register(LegendsApphook)
