from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_menus import ManagerMenu


class ManagerApphook(CMSApp):
    name = _('Manager')
    urls = ['colegend.manager.urls']
    menus = [ManagerMenu]


apphook_pool.register(ManagerApphook)
