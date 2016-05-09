from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_menus import TestMenu


class StyleguideApphook(CMSApp):
    name = _('Styleguide')
    urls = ['colegend.styleguide.urls']
    menus = [TestMenu]


apphook_pool.register(StyleguideApphook)
