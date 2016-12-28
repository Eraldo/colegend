from colegend.components.models import Component


class DemoComponent(Component):
    def get_context(self, context, title='legend', **kwargs):
        context['foo'] = 'Hello {title} {name}'.format(name=context.get('user') or 'you', title=title)
        return context
