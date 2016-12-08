from django import template
from colegend.components.components import Component

register = template.Library()


class DemoComponent(Component):
    def render_component(self, context, page):
        return 'Hello {user} on {page} page'.format(
            user=context.get('user') or 'anonymous',
            page=page
        )


register.tag(DemoComponent())
