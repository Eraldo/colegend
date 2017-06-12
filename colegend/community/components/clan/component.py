from colegend.community.models import ClanPage
from colegend.components.models import Component


class ClanComponent(Component):
    def get_context(self, context, clan=None, **kwargs):
        clan = clan or context.get('clan')
        context['clan'] = clan
        user = context.get('user')
        if user and user.is_authenticated and not user.clan:
            clan_page = ClanPage.objects.first()
            if clan_page:
                url = clan_page.url
                context['join_url'] = url + clan_page.reverse_subpage('join')
        return context
