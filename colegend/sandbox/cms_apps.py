from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SandboxApphook(CMSApp):
    name = _('Sandbox')
    urls = ['colegend.sandbox.urls']


apphook_pool.register(SandboxApphook)
