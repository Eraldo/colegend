from django import template

from colegend.office.components.focus.component import FocusComponent

register = template.Library()

register.tag(FocusComponent.as_tag())
