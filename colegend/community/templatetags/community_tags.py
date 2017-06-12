from django import template

from colegend.community.components.clan.component import ClanComponent
from colegend.community.components.duo.component import DuoComponent
from colegend.community.components.tribe.component import TribeComponent

register = template.Library()

register.tag(DuoComponent.as_tag())
register.tag(ClanComponent.as_tag())
register.tag(TribeComponent.as_tag())
