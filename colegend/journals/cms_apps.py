from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class JournalApphook(CMSApp):
    name = _('Journal')
    urls = ['colegend.journals.urls']


apphook_pool.register(JournalApphook)
