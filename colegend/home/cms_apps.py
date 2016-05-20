from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class HomeApphook(CMSApp):
    name = _('Home')
    urls = ['colegend.home.urls']


apphook_pool.register(HomeApphook)
