from colegend.components.models import Component
from colegend.journals.scopes import Day


class FocusComponent(Component):
    def get_context(self, context, focus=None, scope=None, **kwargs):
        if not focus:
            user = context.get('user')
            if user:
                try:
                    scope = scope or Day()
                    focus = user.focuses.get(scope=scope.name, start=scope.start)
                except:
                    return context
        context['focus'] = focus
        return context
