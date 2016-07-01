from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template

register = template.Library()


@register.tag
class Menu(InclusionTag):
    name = 'menu'
    template = 'widgets/navigation.html'
    options = Options(
        Argument('root', required=False),
    )

    # def get_node(self, page, current_page, ancestors):
    #     return {
    #         'text': page.title,
    #         'href': page.url if not page == current_page else None,
    #     }
    #
    # def get_nodes(self, context):
    #     current_page = context.get('page')
    #     if current_page:
    #         current_page = current_page.specific
    #         ancestors = current_page.get_ancestors().live().in_menu().specific()
    #         return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
    #             self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
    #     else:
    #         return []

    def get_context(self, context, root, **kwargs):
        nodes = []
        if root:
            pages = root.get_children().live().in_menu()
            nodes = pages
        return {
            'nodes': nodes,
            'page': context.get('page'),
        }


# @register.tag
# class Breadcrumb(InclusionTag):
#     name = 'breadcrumb'
#     template = 'widgets/breadcrumb.html'
#
#     def get_node(self, page, current_page, ancestors):
#         return {
#             'text': page.title,
#             'href': page.url if not page == current_page else None,
#         }
#
#     def get_nodes(self, context):
#         current_page = context.get('page')
#         if current_page:
#             current_page = current_page.specific
#             ancestors = current_page.get_ancestors().live().in_menu().specific()
#             return [self.get_node(page, current_page=current_page, ancestors=ancestors) for page in ancestors] + [
#                 self.get_node(current_page, current_page=current_page, ancestors=ancestors)]
#         else:
#             return []
#
#     def get_context(self, context, **kwargs):
#         nodes = self.get_nodes(context)
#         return {'links': nodes}
