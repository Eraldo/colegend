from colegend.components.models import Component


class CardHeaderComponent(Component):
    is_block = True

    def get_context(self, context, content='', **kwargs):
        context.update({
            'content': content,
        })
        return context


class CardComponent(Component):
    is_block = True
    directives = [CardHeaderComponent]

    def get_context(self, context, content='', header='', title='', footer='', url='', actions='', classes='', **kwargs):
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


# class NewCardComponent(Component):
#     # blocks = ['newcard']
#
#     def get_context(self, context, content, header='', title='', footer='', url='', actions='', classes='', **kwargs):
#         context.update({
#             'header': header,
#             'content': content,
#             'title': title,
#             'footer': footer,
#             'url': url,
#             'actions': actions,
#             'classes': classes,
#         })
#         return context
