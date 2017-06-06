from django.conf import settings
from wagtail.wagtailcore.models import Page


class WelcomePage(Page):
    template = 'welcome/base.html'

    parent_page_types = ['cms.RootPage']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if settings.ACCOUNT_ALLOW_REGISTRATION:
            context['open'] = True
        return context
