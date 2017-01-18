from django import template

from colegend.components.components.demo.component import DemoComponent

register = template.Library()

register.tag(DemoComponent.as_tag())
