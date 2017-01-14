from colegend.components.models import Component


class TribeComponent(Component):
    def render(self, context, tribe=None):
        tribe = tribe or context.get('tribe')
        return tribe


class ClanComponent(Component):
    def render(self, context, clan=None):
        clan = clan or context.get('clan')
        return clan


class DuoComponent(Component):
    def render(self, context, duo=None):
        duo = duo or context.get('duo')
        return duo
