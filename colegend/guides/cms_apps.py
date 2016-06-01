from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GuidesApphook(CMSApp):
    name = _('Guides')
    urls = ['colegend.guides.urls']


apphook_pool.register(GuidesApphook)
