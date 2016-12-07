from django import template
from colegend.components.components import Component

register = template.Library()


class DemoComponent(Component):
    def render_component(self, context, page):
        return 'Hello World {0}'.format(page)


register.tag(DemoComponent())
