from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class AboutApphook(CMSApp):
    name = _('About')
    urls = ['colegend.about.urls']


apphook_pool.register(AboutApphook)
