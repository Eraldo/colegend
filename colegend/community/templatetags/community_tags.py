from django import template

from colegend.community.components.duo.component import DuoComponent

register = template.Library()

# register.tag(TribeComponent.as_tag())
# register.tag(ClanComponent.as_tag())
register.tag(DuoComponent.as_tag())
