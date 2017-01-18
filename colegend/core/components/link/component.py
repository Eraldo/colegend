from colegend.components.models import Component


class LinkComponent(Component):
    def get_context(self, context, content, url, external=False, unstyled=False, classes='', **kwargs):
        if unstyled:
            classes += ' unstyled'
        context.update({
            'content': content,
            'url': url,
            'external': external,
            'classes': classes,
        })
        return context
