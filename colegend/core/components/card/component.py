from colegend.components.models import Component


class CardComponent(Component):
    def get_context(self, context, content, header='', title='', footer='', url='', actions='', classes='', **kwargs):
        context.update({
            'header': header,
            'content': content,
            'title': title,
            'footer': footer,
            'url': url,
            'actions': actions,
            'classes': classes,
        })
        return context
