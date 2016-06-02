from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SupportApphook(CMSApp):
    name = _('Support')
    urls = ['colegend.support.urls']


apphook_pool.register(SupportApphook)
