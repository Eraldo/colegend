from colegend.community.models import DuoPage
from colegend.components.models import Component


class DuoComponent(Component):
    def get_context(self, context, duo=None, **kwargs):
        duo = duo or context.get('duo')
        context['duo'] = duo
        user = context.get('user')
        if user and user.is_authenticated and not user.duo:
            duo_page = DuoPage.objects.first()
            if duo_page:
                url = duo_page.url
                context['join_url'] = url + duo_page.reverse_subpage('join')
        return context
