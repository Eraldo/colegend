from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class StoryApphook(CMSApp):
    name = _('Story')
    urls = ['colegend.story.urls']


apphook_pool.register(StoryApphook)
