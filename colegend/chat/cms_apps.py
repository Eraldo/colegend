from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ChatApphook(CMSApp):
    name = _('Chat')
    urls = ['colegend.chat.urls']


apphook_pool.register(ChatApphook)
