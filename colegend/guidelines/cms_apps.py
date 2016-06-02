from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GuidelinesApphook(CMSApp):
    name = _('Guidelines')
    urls = ['colegend.guidelines.urls']


apphook_pool.register(GuidelinesApphook)
