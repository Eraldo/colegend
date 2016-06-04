from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

# from .cms_menus import VisonMenu


class VisionsApphook(CMSApp):
    name = _('Visions')
    urls = ['colegend.visions.urls']
    # menus = [VisonMenu]


apphook_pool.register(VisionsApphook)
