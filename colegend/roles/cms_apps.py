from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class RolesApphook(CMSApp):
    name = _('Roles')
    urls = ['colegend.roles.urls']


apphook_pool.register(RolesApphook)
