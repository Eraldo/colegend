from colegend.community.models import TribePage
from colegend.components.models import Component


class TribeComponent(Component):
    def get_context(self, context, tribe=None, **kwargs):
        tribe = tribe or context.get('tribe')
        context['tribe'] = tribe
        user = context.get('user')
        if user and user.is_authenticated and not user.tribe:
            tribe_page = TribePage.objects.first()
            if tribe_page:
                url = tribe_page.url
                context['join_url'] = url + tribe_page.reverse_subpage('join')
        return context
